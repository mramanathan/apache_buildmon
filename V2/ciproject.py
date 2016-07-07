#!/usr/bin/env python

# -*- coding: utf-8 -*-

import argparse
import logging
import sys
from citool import Citool


def projectInfo(projectName):
    
    # For 'projectName', get info about the last completed build and the last 10 builds.
    
    jenkins = Citool()
    logging.info("Checking %s in project list..." %(projectName))
    jenkins.showBuildStatus(projectName)
    
    return ''


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description="Help to track the CI status of projects hosted at tcloud-sofia.rds.intel.com")
    parser.add_argument("-v", "--verbosity", default=0, action="store_true", help="Output debug messages")
    parser.add_argument("-d", "--dump", metavar="all", action="store", help="List all Tcloud Jenkins project")
    parser.add_argument("-s", "--show", metavar="project-name", action="store", help="Show details (status of last completed build, quick summary of last 10 builds) about the specified project")
    parsed_args = parser.parse_args()

    logLevel = logging.INFO
    if parsed_args.verbosity:
        logLevel = logging.DEBUG

    logFormat = "{{ %(asctime)s  == %(levelname)-8s  ==Module:%(module)s  Function:%(funcName)s Line:%(lineno)d }} %(message)s "
    logging.basicConfig(level=logLevel, format=logFormat, datefmt='%m/%d/%Y %I:%M:%S %p')

    if parsed_args.dump:
        jenkins = Citool()
        jenkins.query()
        
    if parsed_args.show:
        projectName = parsed_args.show.upper()
        projectInfo(projectName)