#!/usr/bin/env python

# -*- coding: utf-8 -*-

import argparse
from citool import Citool


def projectQuery(queryString):
    
    # List all projects that contain this 'queryString'
    
    jenkins = Citool(proxyset, parsed_args.verbosity)
    jenkins.showProjects(queryString)
    
    return ''


def projectInfo(projectName):
    
    # For 'projectName', get info about the last completed build and the last 10 builds.
    
    jenkins = Citool(proxyset, parsed_args.verbosity)
    jenkins.showBuildStatus(projectName)
    
    return ''


if __name__ == '__main__':
    
    parser = argparse.ArgumentParser(description="Help to track the CI status of projects hosted at apache.org")
    parser.add_argument("-v", "--verbosity", type=int, default=0, choices=[0, 1, 2], help="print debugging output")
    parser.add_argument("-p", "--proxy", default="off", choices=["on", "off"], help="Jenkins access outside the corporate network")
    parser.add_argument("-d", "--dump", metavar="all", action="store", help="List all Apache project")
    parser.add_argument("-q", "--query", metavar="project-name", action="store", help="List projects that match this project name")
    parser.add_argument("-s", "--show", metavar="project-name", action="store", help="List build status for the specified project")
    parsed_args = parser.parse_args()

    if parsed_args.proxy:
        proxyset = parsed_args.proxy.upper()
        
    if parsed_args.dump:
        jenkins = Citool(proxyset, parsed_args.verbosity)
        jenkins.query()
        
    if parsed_args.query:
        projectQuery(parsed_args.query)
        
    if parsed_args.show:
        projectName = parsed_args.show
        projectInfo(projectName)