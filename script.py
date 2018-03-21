#!/usr/bin/python

import os # operating system related task- file/directory/process handling, etc...
import re #matching/finding/searching/grouping operations
import sys #system specific parameters and functions- path, argv, stdout etc...
import subprocess #allows to start new process and obtain return values- ex. compiling codes in terminal, etc..



replace_buffer = []
attempt = 1


def main():
    global attempt
        
      
    count = 0
    flag = 0
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
        print "Timing violation occured"
        change_clk(count)
    elif slack_value==0 and attempt!=0:
        change_clk(count)
#        main()
    else:
        print "ALl done with smile"
        flag=1
    #print "count is:"    
    #print count
    report.close()
    
    
    
def change_clk(count2):
    script = open("synthesis.script", "r+")
    global replace_buffer
    
    for xyz in script:
        if 'create_clock' in xyz:
            value = re.search(r'\d+\.\d+|\d+', xyz).group()
            value_f = float(value)
            #print "value_f is:"
            #print value_f
            
            if count2==5:
                new_value = value_f - 0.2
            else:
                new_value = value_f + 0.2
            
            new_value = str(new_value)
            xyz = xyz.replace(value, new_value)
            #print xyz
#        with open("synthesis.script", "w+") as f:
#            f.write(file_str)
        
        write_to_file(xyz)
#        
    replace_buffer = []
#    print replace_buffer
    script.close()





def write_to_file(lmn):
    global replace_buffer
    replace_buffer.append(lmn)
    #print replace_buffer
    
    s1 = open("synthesis.script", "w")
#    s.write(replace_buffer)
    sys.stdout = s1
#    
    for item in replace_buffer:
#        s.replace (value)
        sys.stdout.write(item)
#        
    s1.close()
    
    

    #run_synthesis()
if __name__ == '__main__':
    main()
    
    
