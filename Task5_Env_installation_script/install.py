#!/usr/bin/env python3

#===============================================================================
# SCRIPT TO INSTALL THE APP EXPERTS ENVIRONMENT
# The script install the following:
# Python 3.6.8, pip, selenium
# Java JDK 1.8
# Eclipse
#===============================================================================
import multiprocessing
import os
from python import install_python;
from java import install_java;
from eclipse import install_eclipse;

def run_tests():
    _ = os.system('python -m unittest install_test');
    
if __name__ == '__main__':
    print("Starting environment installation")
    jobs = []
     
    # Python process
    a = multiprocessing.Process(target=install_python)
    jobs.append(a)
    a.start()
    # Java process
    b = multiprocessing.Process(target=install_java)
    jobs.append(b)
    b.start()
    # Eclipse process
    c = multiprocessing.Process(target=install_eclipse)
    jobs.append(c)
    c.start()
    
    a.join()
    b.join()
    c.join()
    
    # Run tests
    run_tests()
     
