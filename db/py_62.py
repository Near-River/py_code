#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pymysql
import pymysql.cursors

# Mysql:
# Connect to the database
connection = pymysql.connect(host='localhost',
                             user='root',
                             password='123456',
                             db='near',
                             charset='utf8mb4',
                             cursorclass=pymysql.cursors.DictCursor)

try:
    with connection.cursor() as cursor:
        # Create a new record
        sql = "INSERT INTO `t_user` (`ID`, `NAME`, `PASSWORD`) VALUES (%s, %s, %s)"
        cursor.execute(sql, (10, 'Nate_River', 'admin'))

    # connection is not autocommit by default. So you must commit to save your changes.
    connection.commit()

    with connection.cursor() as cursor:
        # Read a single record
        sql = "SELECT `ID`, `NAME`, `PASSWORD` FROM `t_user` WHERE `ID`=%s"
        cursor.execute(sql, (10,))
        result = cursor.fetchone()  # Fetches one row from the result set
        print(result)
finally:
    connection.close()
