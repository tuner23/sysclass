#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Python Classes
#import os
import sys
from optparse import OptionParser

## Own Classes
## TODO: Move to /lib
from lib.sysclass import SysClass
from lib.skeleton_class import MyApp


## Allow multiline descriptions
class MyOptionParser(OptionParser):
    def format_description(self, formatter):
        return self.get_description()
    def format_epilog(self, formatter):
        return self.expand_prog_name(self.epilog)

## Parse Options
parser = MyOptionParser(  "Usage: %prog   [OPTIONS]",
            description = """\
MyApp - Skeleton for Python

Skeleton for new scripts including logging, configfile parsing and more..
""",
            version = "0.9",
            epilog = """
Examples:
    Some examples:
        %prog -h
        %prog -C -D
""" 
)

default = './conf.d/'
parser.add_option(      "-C", "--config",
            dest ="config",
            default = default,
            help = "Location of the configfile(s) (default: " + default + "). Includes all *.conf files inside directory.")

default = './log.d/default.log'
parser.add_option(      "-L", "--logging",
            dest ="log",
            default = default,
            help = "Location of the logfile (default: " + default + ").")

parser.add_option(      "-V", "--verbose",
            dest ="verbosity",
            action="store_true",
            default=False,
            help ="Verbose output")

parser.add_option(      "-D", "--debug",
            dest ="debug",
            action="store_true",
            default=False,
            help ="Enable debugging")

default = "main"
parser.add_option(      "-S", "--section",
            dest ="section",
            default="main",
            help ="Select the main section of the main configuration file used to store sysclass variables. (default: " + default + ").")

if len(sys.argv)==1:
    parser.print_help()
    sys.exit(1)


def main(argv=None):
    ### Get Options and initialize system class
    sysclass = SysClass(parser)

    ### Do somethin
    cmpObj = MyApp(sysclass)
    cmpObj.F()



if __name__ == "__main__":
    main()

# EOF
# vim:foldmethod=marker:tabstop=3:autoindent:shiftwidth=3