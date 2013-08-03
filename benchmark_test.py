#!/usr/bin/env python
"""
The bench mark test script will check how much time is taken for a 
Python Script to run from start to end. Telling its performance in hours mins and secs.
The tool can take in two types of input.
1. Get scripts from a file
2. Get the script from command line.

The tool supports multiple scripts to be run through file.
Commandline run supports only single script to be run.
The tool is still under Test

Enhancements (TBD):
------------
1. Implement KeyboardInterrupt handling properly
2. Commandline execution. Support multiple scripts in commandline
3. More Proper Error handling
4. Use argparse for handling commandline arguements.
"""
import os, sys, time

def get_tests_from_file():
    """This Method will get the scripts to be executed from the file
    config.txt. Please follow the following syntax in file
    <script1> <cmdlineargs>
    <script2> <cmdlineargs>
    """
    try:
        script_file = open('config.txt')
        cmds = [script.strip() for script in script_file.readlines()]
        return cmds
    finally:
        script_file.close()
            
def get_test_from_cmd_line(cline_args):
    # Abstract method if cmd line execution needs to be changed
    print "Under dev"
    
def calculate(ps, stime, etime):
    """This Method Calculates the time taken for the script to run. 
    Gets the start and End time and computes the runtime.
    @param ps: It is the script command ran
    @param stime: Time when script was started
    @param etime: Time when script got ended
    """
    if etime[2] < stime[2]:
        hours, mins, secs = (etime[0] - stime[0], etime[1] - stime[1], 
                             etime[2])
    else:
        hours, mins, secs = (etime[0] - stime[0], etime[1] - stime[1], 
                             etime[2] - stime[2])
    print "The Script %s has run for %s Hours %s Minutes %s Seconds" % (ps.split()[1], 
                                                                        hours, mins,
                                                                        secs)
        
def test(pscmds):
    """The Actual method which triggers the scripts and 
    captures the start and end time.
    @param pscmds: List of python script commands to be run
    """
    try:
        for pscript in pscmds:
            pscript = 'python ' + pscript
            ts = time.localtime() 
            starttime = [ts.tm_hour, ts.tm_min, ts.tm_sec]
            print "BENCHMARK Startime is, %s hrs : %s mins : %s secs" % (ts.tm_hour,
                                                                         ts.tm_min,
                                                                         ts.tm_sec)
            print "*"*60
            os.system(pscript)
            te = time.localtime()
            endtime = [te.tm_hour, te.tm_min, te.tm_sec]
            print "BENCHMARK Endtime is, %s hrs : %s mins : %s secs" % (te.tm_hour,
                                                                        te.tm_min, 
                                                                        te.tm_sec)
            print "*"*60
            calculate(pscript, starttime, endtime)
            
    except KeyboardInterrupt:
        print "User Interrupted the execution. Benchmark test Aborted"
        endtime = [te.tm_hour, te.tm_min, te.tm_sec]
        print "Aorted Endtime is, %s hrs : %s mins : %s secs" % (te.tm_hour,
                                                                 te.tm_min, 
                                                                 te.tm_sec)
    
def main():
    """This Method handles the Arguements and Triggers test() for the benchmark"""
    args = sys.argv
    if '-f' in args and '-c' in args:
        raise Exception("Cannot have both -f and -c at same time")
    try:
        if '-f' in args or len(args) < 2:
            if os.path.exists("config.txt"):
                scmds = get_tests_from_file()
    except OSError, err:
        print "No Config File found : ", err
    if '-c' in args:
        scmds = [' '.join(args[2:])]
    test(scmds)
    
    
if __name__ == '__main__':
    main()
