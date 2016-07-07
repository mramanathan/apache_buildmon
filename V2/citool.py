#!/usr/bin/env python

# -*- coding: utf-8 -*-

from urllib2 import urlopen
import re
import sys
import collections


class Citool(object):
    
    # Base class that implements query of Tcloud jenkins
    
    def __init__(self):
        
        # URL parts that shall be used by the various methods
        
        self.pyapi = 'api/python?pretty=true'
        self.buildurl = 'https://builds.apache.org/'
        
        
        
    def query(self, *thisProject):
        
        """ If 'thisProject' is empty, list all project names setup in Tcloud Jenkins
        
        If 'thisProject' is invalid, quit with message.
        If 'thisProject' is given, return project's tcloud jenkins URL.
        """
        
        allProjects = eval(urlopen(self.buildurl + self.pyapi).read())
        
        if len(thisProject) == 0:
            for project in allProjects['jobs']:
                print project.get('name')
            return ''
        elif thisProject[0]:
            print("Checking %s in project list..." %(thisProject[0]))
            for i in allProjects['jobs']:
                if thisProject[0] == i['name']:
                    print("Matched {0} with {1}".format(thisProject[0], i['name']))
                    print("Project URL to access more info is {}".format(i['url']))
                    return i['url']
            else:
                print("Invalid project, %s, exiting now." %(thisProject[0]))
                return ''
                sys.exit()


    
    def getBuildCause(self, buildInfo):
        
        # From 'buildInfo' data structure, return the event that triggered the build.
        
        self.buildInfo = buildInfo
        
        for i in buildInfo['actions']:
            if i.has_key('causes'):
                causeInfo = i['causes']
                break
                
        for j in causeInfo:
            if j.has_key('shortDescription'):
                buildCause = j['shortDescription']
                break
        
        buildCause = re.sub("Started by ", "", buildCause)
        
        return buildCause
    
    
    
    def showLatestBuild(self, projectInfo):
        
        """ Using the 'projectInfo' (REST API output), get the following:
        
        URL of the last completed build and what event triggered this build.
        """
        
        print("Last completed build of {0} is {1}".format(self.projectName, projectInfo['lastCompletedBuild']['url']))
        lastBuildInfo = eval(urlopen(projectInfo['lastCompletedBuild']['url'] + self.pyapi).read())
        
        startedBy = self.getBuildCause(lastBuildInfo)
        if lastBuildInfo['building'] == False and lastBuildInfo['result'] == "SUCCESS":
            print("Build was started by {0}".format(startedBy))
            print("And the build passed without any errors")
        if lastBuildInfo['building'] == False and lastBuildInfo['result'] == "FAILURE":
            print("Build was started by {0}".format(startedBy))
            print("And the build failed with errors")
        if lastBuildInfo['building'] == False and lastBuildInfo['result'] == "ABORTED":
            print("Build was started by {0}".format(startedBy))
            print("And the build was aborted")
        
<<<<<<< 595b0812dd24bd6b3b678c87dca955363338ae2e:V2/citool_query.py
        return ''
    
    
    def showLastTen(self, projectInfo):
        
        """ Using the 'projectInfo' (REST API output), get the following:
        
        short stat on the completion status of the last 10 builds for this project.
        """
        
        counter = 1
        buildStats = collections.OrderedDict()
        buildUrls = []
        buildResult = []
        
        allBuilds = projectInfo['builds']
        
        for b in allBuilds:
            if counter <= 10:
                thisBuildInfo = eval(urlopen(b['url'] + self.pyapi).read())
                buildUrls.append(b['url'])
                if thisBuildInfo['building'] == True:
                    buildResult.append("Build in progress")
                else:
                    buildResult.append(thisBuildInfo['result'])
            counter += 1
            
        for job, status in zip(buildUrls, buildResult):
            print("Status of build job, {0} is, {1}".format(job, status))
            buildStats.update({job : status})
            
        return ''
    
    
    def showBuildStatus(self, projectName):
        
        """ For 'projectName', query tcloud jenkins and extract details
        
        of the staus of last completed build and short statistics of
        the last 10 completed builds.
        """
        
        self.projectName = projectName
        projectUrl = self.query(self.projectName)
        
        newBuildurl = projectUrl + "/" + self.pyapi
        projectInfo = eval(urlopen(newBuildurl).read())
        
        self.showLatestBuild(projectInfo)
        self.showLastTen(projectInfo)

        return ''
