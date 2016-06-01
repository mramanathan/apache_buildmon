
# coding: utf-8

# In[22]:

from jenkinsapi import api
import MySQLdb
from collections import OrderedDict


global jenkinsUrl
global projectInfo

jenkinsUrl = 'https://builds.apache.org/api/python'
projectInfo = OrderedDict()


def jenkinsBase(url):
    
    """
    param  : jenkins url
    Prepare the Python API call to jenkins url
    return : pass the newly created object 
    
    nOTE : anaonymous access works for https://builds.apache.org
    TODO : Howto code for authentication using APItoken with Python >3.x 
    """
    jobInfo = api.Jenkins(url)
    
    return jobInfo


def mysqlConnect():
    
    """
    Connect to mysql database using the given data
    param : none
    return : dbconnector and it's cursor objects
    """
    
    mysqlHost = "pysql.c242rwjvadxq.us-west-2.rds.amazonaws.com"
    mysqlUser = "pysql"
    mysqlPass = "pysql1729#"
    mysqlDB   = "apache_buildmon"
    
    dbConn = MySQLdb.connect(mysqlHost, mysqlUser, mysqlPass, mysqlDB)
    
    cursor = dbConn.cursor()
    
    return dbConn,cursor


def updateProjectIndB(jobInfo, dbConn, cursor):
    
    """
    param : jobinfo object to extract project details, mysql connection plugs
    Retrieve project name and URL using get_jobs_info() method of jenkinsapi.
    Save the data in an ordered dict, and also commit in mysql dB.
        
    return : none
    """
    
    for info in jobInfo.get_jobs_info():
        # print info[1], info[0]
        projectInfo.update({info[1] : info[0]})
        cursor.execute("""INSERT INTO Project (name, url) VALUES(%s, %s)""",
                        (info[1], info[0]))
        dbConn.commit()
    
    cursor.execute("SELECT * FROM Project LIMIT 15,20")
    
    projectData = cursor.fetchall()
    print(projectData)    
       
    return ''


def main():
    """
    Main function to invoke connection requests to services, like, jenkins, mysql database.
    Use the returned objects to gather build details and push to database.
    """
    
    jobInfo = jenkinsBase(jenkinsUrl)
    dbConn,cursor = mysqlConnect()
    updateProjectIndB(jobInfo, dbConn, cursor)
    
if __name__ == '__main__':
    main()


# In[17]:

print type(projectData)


# In[ ]:



