#!/usr/bin/env python

# -*- coding: utf-8 -*-

import argparse
import logging
import sys
from citool import Citool


def projectInfo(projectName):
    
    # For 'projectName', get info about the last completed build and the last 10 builds.
    
    jenkins = Citool(proxyset)
    logging.info("Checking %s in project list..." %(projectName))
    jenkins.showBuildStatus(projectName)
    
    return ''


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description="Help to track the CI status of projects hosted at apache.org")
    parser.add_argument("-v", "--verbosity", type=int, default=0, choices=[0, 1, 2], help="print debugging output")
    parser.add_argument("-d", "--dump", metavar="all", action="store", help="List all Apache project")
    parser.add_argument("-p", "--proxy", default="off", choices=["on", "off"], help="Jenkins access outside the corporate network")
    parser.add_argument("-s", "--show", metavar="project-name", action="store", help="List build status for the specified project")
    parsed_args = parser.parse_args()

    if parsed_args.verbosity == 0:
        logLevel = logging.INFO
    if parsed_args.verbosity == 1:
        logLevel = logging.WARNING
    if parsed_args.verbosity == 2:
        logLevel = logging.DEBUG

    logFormat = "{{ %(asctime)s  == %(levelname)-8s  ==Module:%(module)s  Function:%(funcName)s Line:%(lineno)d }} %(message)s "
    logging.basicConfig(level=logLevel, format=logFormat, datefmt='%m/%d/%Y %I:%M:%S %p')

    if parsed_args.proxy:
        proxyset = parsed_args.proxy.upper()
        
    if parsed_args.dump:
        jenkins = Citool(proxyset)
        jenkins.query()
        
    if parsed_args.show:
        projectName = parsed_args.show
        projectInfo(projectName)
