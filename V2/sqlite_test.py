#!/usr/bin/env python

# -*- coding: utf-8 -*-

import sqlite3
import random
import datetime
import time

dbName = 'sqlite_test.db'
with sqlite3.connect(dbName) as sqlConn:
    sqlCursor = sqlConn.cursor()

def create_table():
    sqlCursor.execute('CREATE TABLE IF NOT EXISTS gitLog(sha1 TEXT, message TEXT)')
    
def populate_data(count):
    # sha1 is randomly generated number in the range 15..35
    # commit message includes today's date and time
    
    sha1 = random.randrange(15,35)
    today = datetime.datetime.today()
    localTime = today.strftime('%Y-%m-%d %H:%M')
    message = str(count) +  " commit with SHA-1 id " + str(sha1) + "made at " + str(localTime)
    sqlCursor.execute("INSERT INTO gitLog (sha1, message) VALUES(?, ?)", (sha1, message))
    sqlConn.commit()
    
def main():
    # table created once, data inserted 10 times with sleep of 5 seconds
    create_table()
    for i in range(10):
        populate_data(i)
        time.sleep(5)
        
    sqlCursor.close()
    sqlConn.close()
    
if __name__ == '__main__':
    main()