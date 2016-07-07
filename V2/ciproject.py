#!/usr/bin/env python

# -*- coding: utf-8 -*-

import argparse
import logging
import sys
from citool_query import Citool

def listProjects():
    
    """
    """
    
    apache = Citool()
    getProjects = apache.queryAll()
    for project in getProjects['jobs']:
        print project.get('name')

    return ''


def showProject(projectName):
    
    """
    """
    
    apache = Citool()
    allProjects = apache.queryAll()
    logging.info("Checking %s in project list..." %(projectName))
    for i in allProjects['jobs']:
        if projectName == i['name']:
            logging.info("Matched {0} with {1}".format(projectName, i['name']))
            print("URL to access info for {0} is {1}".format(projectName, i['url']))
            apache.showBuildStatus(projectName, i['url'])
            sys.exit()
    else:
        print("Invalid project, %s, exiting now." %(projectName))
        sys.exit()
    
    return ''


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description="Help to track the CI status of projects hosted at apache.org")
    parser.add_argument("-v", "--verbosity", default=0, action="store_true", help="print debugging output")
    parser.add_argument("-d", "--dump", metavar="all", action="store", help="List all Apache project")
    parser.add_argument("-s", "--show", metavar="project-name", action="store", help="List build status for the specified project")
#   parser.add_argument("-l", "--list", action="store", help="List all Apache project")
#   parser.add_argument("-s", "--show", action="store", help="List build status for the specified project")
    parsed_args = parser.parse_args()

    logLevel = logging.INFO
    if parsed_args.verbosity:
        logLevel = logging.DEBUG

    logFormat = "{{ %(asctime)s  == %(levelname)-8s  ==Module:%(module)s  Function:%(funcName)s Line:%(lineno)d }} %(message)s "
    logging.basicConfig(level=logLevel, format=logFormat, datefmt='%m/%d/%Y %I:%M:%S %p')

    if parsed_args.dump:
        listProjects()
        
    if parsed_args.show:
        projectName = parsed_args.show.upper()
        showProject(projectName)