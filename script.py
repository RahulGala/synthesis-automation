#!/usr/bin/python



import os # operating system related task- file/directory/process handling, etc...

import re #matching/finding/searching/grouping operations

import sys #system specific parameters and functions- path, argv, stdout etc...

import subprocess #allows to start new process and obtain return values- ex. compiling codes in terminal, etc..

import time





replace_buffer = []

attempt = 1


p_flag =0

n_flag =0

flag=0


def main():

    global attempt

    global p_flag
    global n_flag
        

      

    count = 0

    
    report = open("synres.txt", "r")

#    print report.read()

    for abc in report:

        if 'slack (MET)' in abc:

            svalue = re.search(r'-?\d+\.\d+|\d+\d+', abc).group()

            slack_value = float(svalue)

            print "slack_value is:"

            print slack_value

            

#            count =+ 1

#            print abc

    

    if slack_value<0:
        attempt =0
        n_flag=1
        print "Timing violation occured"
        change_clk(count)
        subprocess.call(["python script.py"], shell=True)

    elif slack_value>2:

        p_flag=1
        change_clk(count)
        subprocess.call(["python script.py"], shell=True)
#        main()

    else:

        print "ALl done with smile"
        flag=1

    #print "count is:"    

    #print count

    report.close()

#    
#if flag!=1:
#         os.exec*()
    

    

    

def change_clk(count2):

    script = open("synthesis.script", "r+")

    global replace_buffer

    global p_flag
    global n_flag
    

    for xyz in script:

        if 'create_clock' in xyz:

            value = re.search(r'\d+\.\d+|\d+', xyz).group()

            value_f = float(value)

            #print "value_f is:"

            #print value_f

            

            if p_flag==1:

                new_value = value_f - 0.2

            elif n_flag==1:

                new_value = value_f + 0.2

            

            new_value = str(new_value)

            xyz = xyz.replace(value, new_value)

            #print xyz

#        with open("synthesis.script", "w+") as f:

#            f.write(file_str)

        

        write_to_file(xyz)

#       

    time.sleep(10)

    synthesize()     



    replace_buffer = []

#    print replace_buffer

    script.close()











def write_to_file(lmn):

    global replace_buffer

    sflag=1

    replace_buffer.append(lmn)

    #print replace_buffer

    

    s1 = open("synthesis.script", "w")

#    s.write(replace_buffer)

    sys.stdout = s1

#    

    for item in replace_buffer:

#        s.replace (value)

        sys.stdout.write(item)

    s1.close()

    

    



def synthesize():

   subprocess.call(["dc_shell -f synthesis.script | tee synres.txt"], shell=True)

    









    #run_synthesis()

if __name__ == '__main__':

    main()

    

    

