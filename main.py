#!/usr/bin/env python
# -*- coding: utf-8 -*-

## Python Classes
import os
import sys
from optparse import OptionParser

## Own Classes
from systemclass import SystemClass
from myapp import MyApp


## Allow multiline descriptions
class MyOptionParser(OptionParser):
    def format_description(self, formatter):
        return self.get_description()
    def format_epilog(self, formatter):
        return self.expand_prog_name(self.epilog)

## Parse Options
parser = MyOptionParser(  "%prog   [OPTIONS]",
            description = """\
MyApp - Dummy

Skeleton for new software using sysclass
""",
            version = "0.9",
            epilog = """
Examples:
    Some examples:
        %prog -h
        %prog -C -D
""" 
)

parser.add_option(      "-C", "--config",
            dest ="config",
            default = False,
            action = "store_true",
            help = "Activate config file handling (default: ./conf.d/). \nIncludes all *.conf files inside directory.")

parser.add_option(      "-P", "--config-path",
            dest ="config_path",
            default="./conf.d/",
            help ="Define individual configuration path/file (default: ./conf.d/).")

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

parser.add_option(      "-S", "--section",
            dest ="section",
            default="main",
            help ="Select the main section of the main configuration file (default: main).")



def main(argv=None):
    ### Get Options and initialize system class
    sysclass = SystemClass(parser)

    ### Do somethin
    cmpObj = MyApp(sysclass)
    cmpObj.F()



if __name__ == "__main__":
    main()

# EOF
# vim:foldmethod=marker:tabstop=3:autoindent:shiftwidth=3
