#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""@package systemclass.py
TODO: Documentation for this module.
 
More details.
"""

__author__ = "Antonios Dimtsoudis"
__copyright__ = "Copyright 2014, systemclass"
__license__ = "MIT"
__version__ = "0.9"
__maintainer__ = "Antonios Dimtsoudis"
__email__ = "antonios.dimtsoudis@gmx.de"
 
import os
import sys
import time
import inspect
import ConfigParser
 
## TODO: Documentation of package, class, function
class SysClass:
    def __init__(self,parser):
        """The Constructor.
 
        Draw some Initialization."""
        ## TODO: Initialization without parser (e.g. script example)
        self.parser = parser
 
        ## set some vars
        ################################################################
        ## separators
        self.separator = "## -----------------------------------------------------------------------------"
        self.verboseseparator = "## --Verbose--------------------------------------------------------------------"
        self.debugSeparator = "## --Debug----------------------------------------------------------------------"
 
        ## get options and args
        ################################################################
        (self.options, self.args) = parser.parse_args()

        ## Setup Logs
        ################################################################
        self.messages = {}
 
        ## main section inside configuration files
        ################################################################
        self.main_section = self.options.section

        ## parse config files
        ################################################################
        self.config = self.options.config
        ## find path
        if self.config:
            config_files = []
            ## File/Path destination of the configuration
            if not os.path.exists(self.config):
                msg = str(self.config) + "is not a file or path in current directory. Trying out script location."
                self.add_message(msg, level='WARNING')
                if self.config.startswith('./'):
                    self.config = os.path.dirname(__file__) + '/' + self.config.lstrip('./')
                    if not os.path.exists(self.config):
                        msg = "Sorry, no configuration file found! Use --no-config if you want to disable configfile usage"
                        self.add_message(msg, level='ERROR')
                        raise Exception(msg)

            if os.path.isfile(self.config):
                config_files = [self.config]
            elif os.path.isdir(self.config):
                for f in os.listdir(self.config):
                    if f.endswith(".conf"):
                        config_files.append(self.config.rstrip('/') + '/' + f)
            else:
                self.ErrorExit(self, "Sorry, " + str(self.config_file) + " is neither a directory, nor a file")
            ## List of configuration files to be parsed
            self.config_files = config_files
            self.sysclass_section = "sysclass"
            ## TODO: set in cfg-file or options or 'main'
            self.main_section = self.options.section

            ## ConfigParser object with parsed configuration
            self.configuration = ConfigParser.ConfigParser()
            self.configuration.read(self.config_files)

 
        ## Set debugging and the verbosity
        ################################################################
        ## Get verbosity option
#        if options.verbosity:
        if ((self.options.verbosity) or
          (self.config and
          self.configuration.has_option(self.sysclass_section,'verbose') and
          self.configuration.get(self.sysclass_section,'verbose') == 'True')):
            self.verbose = True
        else:
            self.verbose = False
 
 
        ## Get debugging option
#        if options.debug:
        if ((self.options.debug) or
          (self.config and
          self.configuration.has_option(self.sysclass_section,'debug') and
          self.configuration.get(self.sysclass_section,'debug') == 'True')):
            self.debug = True
            self.verbose = True
        else:
            self.debug = False
        if self.verbose:
            self.BeVerbose("Getting Options:\nVerbose:\t" + str(self.verbose) + "\nDebug:\t" + str(self.debug))
 
 
################################################################
## Functions
################################################################
## TODO: Implement logging in sysclass
    ## Add message logging
    def add_message(self, message, level='INFO'):
        actime = time.time()
        self.messages[actime] = {message: message, level: level}


    ## Throw out message 
    def ThrowMsg(self, output, header=None, msgtype="WARNING"):
        """Throw out message, no matter if verbosity or debugging is set
        """
        print self.separator
        if header:
            print "## " + str(msgtype) + ": " + str(header) + ":"
        else:
            print "## " + str(msgtype) + ": "
        if type(output) is list:
            for value in output:
                print "## " + str(value)
        elif type(output) is str:
            print "## " + str(output)
 

    ## Be Verbose
    def BeVerbose(self, output, header=None):
        """Print given output if verbosity is set.
        """
        if self.verbose:
            print self.verboseseparator
            if header:
                print "## " + header + ":"
            if type(output) is list:
                for value in output:
                    print "## " + str(value)
            elif type(output) is str:
                for line in output.splitlines():
                    print "## " + str(line)

 
    ## Do debugging
    def Debug(self, klass, output, header=None):
        """Print given output if debugging is set.
        """
        if self.debug:
            print self.debugSeparator
            print "## class: " + klass.__class__.__name__ + ",  function: " + inspect.stack()[1][3]
            if header:
                print "## " + header + ":"
            if isinstance(output, list):
                for value in output:
                    print "## " + str(value)
            elif isinstance(output, str):
                for line in output.splitlines():
                    print "## " + str(line)
            else:
                for line in output:
                    print "## " + str(line)

 
    ## Print error message and exit
    def ErrorExit(self, klass, output, header = None):
        """Print the defined error message and exit
        """
        self.debug = True
        self.Debug(klass, output, header=header)
        print "\n\n"
        ## TODO: Evalate True/False to bool when necessary
        ## TODO: sysclass variables should be initialized on init (and don't use main section..)
        try:
            help_on_error = self.GetValue('help_on_error', section='sysclass')
        except:
            help_on_error = False

        if help_on_error == 'True':
            print "xxxx"
            print self.GetValue('help_on_error', section='sysclass')
            self.parser.print_help()
            print "xxxx"
        sys.exit()
 

    ## Get als sections found in the configuration files
    def GetSections(self, cfgfile=None):
        """
        Args:
            cfgfile - specify configuration file
        """
        if cfgfile:
            pass
        else:
            if self.config and self.configuration:
                return self.configuration.sections()
        return False


    ## Get options of sections
    def GetOptions(self, section=None):
        if self.config and section:
            return self.configuration.options(section)
        return False

            
    ## Get value
    def GetValue(self, value, section=None):
        """Try to get value from given data
        Order: cmdline --> defined section --> main section"""
	## TODO: integrate sysclass-section
        result = None
 
        ## Get value from cmdline args
	print "xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx"
        result = getattr(self.options, value, False)
        print result
	if self.config:
	    self.config.get(section, value)

	sys.exit()
        ## Get value from config files
        if not result and self.config:
            if section and self.configuration.has_option(section, value):
                result = self.configuration.get(section, value)
                if not result:
                    section = None
            elif self.configuration.has_option(self.main_section, value):
                result = self.configuration.get(self.main_section, value)
 
        ## Process results
        if result:
            if section:
                self.Debug(self, 'Getting value ' + str(value) + ' from section ' + str(section) + ': ' + str(result))
            else:
                self.Debug(self, 'Getting value ' + str(value) + ' from main section: ' + str(result))
            return result
 
        raise Exception("Value " + str(value) + " not found!")


    ## Get/Set verbosity
    def Verbosity(self, setv=None):
        """
        """
        if setv is not None:
            self.verbose = setv
        return self.verbose
 

    ## Get/Set debugging
    def Debugging(self, setd=None):
        """
        """
        if setd is not None:
            self.debug = setd
        return self.debug
 
# EOF
# vim:foldmethod=marker:tabstop=3:autoindent:shiftwidth=3
