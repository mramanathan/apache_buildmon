#!/usr/bin/env python

# -*- coding: utf-8 -*-

from urllib2 import urlopen
import re
#import collections

#projectData = collections.OrderedDict()

class Citool(object):
    
    def __init__(self):
        
        self.pyapi = 'api/python?pretty=true'
#        self.buildurl = 'https://builds.apache.org/'
        self.buildurl = 'https://tcloud6-sofia.rds.intel.com/b/'
        
    def queryAll(self):
        
        apache_projects = eval(urlopen(self.buildurl + self.pyapi).read())

        return apache_projects
    
    def getBuildCause(self, buildInfo):
        
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
    
    def showBuildStatus(self, projectName, projectUrl):
        
        self.projectName = projectName
        self.projectUrl  = projectUrl
        
        newBuildurl = self.projectUrl + "/" + self.pyapi
        thisProject = eval(urlopen(newBuildurl).read())
        
        print("Last completed build of {0} is {1}".format(self.projectName, thisProject['lastCompletedBuild']['url']))
        lastBuildUrl = eval(urlopen(thisProject['lastCompletedBuild']['url'] + self.pyapi).read())
        startedBy = self.getBuildCause(lastBuildUrl)
        if lastBuildUrl['building'] == False and lastBuildUrl['result'] == "SUCCESS":
            print("Build was started by {0}".format(startedBy))
            print("And the build passed without any errors")
        if lastBuildUrl['building'] == False and lastBuildUrl['result'] == "FAILURE":
            print("Build was started by {0}".format(startedBy))
            print("And the build failed with errors")
        if lastBuildUrl['building'] == False and lastBuildUrl['result'] == "ABORTED":
            print("Build was started by {0}".format(startedBy))
            print("And the build was aborted")
        
        return ''
    
    
#hadoopList = {}

#for thisJob in apache_projects['jobs']:
#    if "Hadoop" in thisJob['name']:
#        print "\n== Project URL : ", thisJob['url']
#        hadoopList.update({thisJob['name'] : thisJob['url']})


#print hadoopList

#print("Apache has {0} Hadoop projects.".format(len(hadoopList.keys())))

#dir(hadoopList)

#hadoop_active_projects = {}

#for hadoopi in hadoopList.iterkeys():
#    # print hadoopList[hadoopi]
#    hadoopPyapi = eval(urlopen(hadoopList[hadoopi] + pyApi).read())
#    try:
#        print("Last completed build of {0} is {1}".format(hadoopi, hadoopPyapi['lastCompletedBuild']['url']))
#        hadoop_active_projects.update({hadoopi : hadoopPyapi['lastCompletedBuild']['url']})
#    except TypeError, ex:
#        print("No valid build data available for {0}".format(hadoopi))


#for hadoopi in hadoop_active_projects.iterkeys():
#    hadoopPyapi = eval(urlopen(hadoop_active_projects[hadoopi] + pyApi).read())
#    print("Build status of the active project, {0} is : {1}".format(hadoopi, hadoopPyapi['result']))