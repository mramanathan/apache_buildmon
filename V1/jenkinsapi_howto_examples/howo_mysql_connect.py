
# coding: utf-8

# In[5]:

import MySQLdb
import time

dbConn = MySQLdb.connect("pysql.c242rwjvadxq.us-west-2.rds.amazonaws.com", 
                         "pysql","pysql1729#","world")

sqlConn = dbConn.cursor()

#username = "Allen Solly"
# tweet = "For the man in you"

""" sqlConn.execute("INSERT INTO tweela (time, username, tweet) VALUES(%s, %s, %s)",
                (time.time(), username, tweet)) """

sqlConn.execute("SHOW TABLES")

dataDump = sqlConn.fetchall()

counter = 1
for i in dataDump:
    ''' works with Python 3.x
    print(i)
    counter=counter+1 '''
    """ Compatible with Python 2.7"""
    print("Data from row {0} is : {1}".format(counter, i))
    counter=counter+1


# In[ ]:



