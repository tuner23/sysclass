#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""@package [PCKGNAME]
Documentation for this module.

More details.
"""

#import os
import sys
#import re


class MyApp:
    ## The Constructor
    def __init__(self,sysclass):
        """
        Draw some Initialization.
        """
        ## Sysclass-Init
        self.sys = sysclass
    
        ## Set program-specific data
        self.sections = self.sys.GetSections()


    ### Public Functions
    ###########################
    ## Example function
    def F(self):
        """
        Show usage by example
        """
        ## verbosity and debugging
        try:
            self._f()
        except:
            self.sys.Debug(self, sys.exc_info()[1])
            #raise "F failed"
            pass

        ## config file handling
        self.sys.BeVerbose("config file handling")
        print "All sections: " + str(self.sections)
        print "Options of 'main' section: " + str(self.sys.GetOptions(section='main'))
        self.sys.Debugging(setd=False)
        print "Getting debug value of default section: " + str(self.sys.GetValue('debug'))
        print "Getting debug value of main section: " + str(self.sys.GetValue('debug', section = 'main'))
        self.sys.Debugging(setd=True)

        self.sys.ErrorExit(self, "Let's exit with an error.. DONE!")
        return True

    ### Internal Functions
    ###########################
    ## short desc
    def _f(self):
        """
        verbose desc
        """
        msg = "Activating verbosity and debugging. Actual state: \nverbosity: " + str(self.sys.Verbosity()) + "\ndebugging: " + str(self.sys.Debugging())
        self.sys.ThrowMsg(msg, msgtype="INFO")

        ## Set verbosity and debugging
        self.sys.Verbosity(setv=True)
        self.sys.Debugging(setd=True)

        self.sys.BeVerbose("Verbosity now activated")
        self.sys.Debug(self, "Debugging now activated")
        
        raise Exception("Subfunction complete!!")
 
if __name__ == '__main__':
    app = MyApp
    a.F()
