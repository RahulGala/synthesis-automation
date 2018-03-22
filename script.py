#!/usr/bin/python
import os 
import re 
import sys 
import subprocess 
import time


replace_buffer = []
p_flag =0
n_flag =0
flag=0


def main():
    global p_flag
    global n_flag
    
    report = open("synres.txt", "r")
    for abc in report:
        if 'slack (MET)' in abc:
            svalue = re.search(r'-?\d+\.\d+|\d+\d+', abc).group()
            slack_value = float(svalue)
            print "slack_value is:"
            print slack_value    

    if slack_value<0:
        n_flag=1
        print "Timing violation occured"
        change_clk()
        subprocess.call(["python script.py"], shell=True)
    elif slack_value>2:
        p_flag=1
        change_clk()
        subprocess.call(["python script.py"], shell=True)
    else:
        print "ALl done with smile"
        flag=1
    report.close()
    


def change_clk():
    script = open("synthesis.script", "r+")
    global replace_buffer
    global p_flag
    global n_flag
    
    for xyz in script:
        if 'create_clock' in xyz:
            value = re.search(r'\d+\.\d+|\d+', xyz).group()
            value_f = float(value)
           
            if p_flag==1:
                new_value = value_f - 0.2
            elif n_flag==1:
                new_value = value_f + 0.2
                
            new_value = str(new_value)
            xyz = xyz.replace(value, new_value)
        write_to_file(xyz)
    time.sleep(5)
    synthesize()     
    replace_buffer = []
    script.close()



def write_to_file(lmn):
    global replace_buffer
    sflag=1
    replace_buffer.append(lmn)
    #print replace_buffer
    s1 = open("synthesis.script", "w")
    sys.stdout = s1
    for item in replace_buffer:
        sys.stdout.write(item)
    s1.close()


def synthesize():
   subprocess.call(["dc_shell -f synthesis.script | tee synres.txt"], shell=True)



if __name__ == '__main__':
    main()

    

    

