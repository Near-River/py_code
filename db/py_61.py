#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sqlite3


# sqlite3:
def createTable():
    # connect to the Sqlite3 database
    conn = sqlite3.connect('demo.db')
    try:
        # create a cursor object
        cursor = conn.cursor()
        try:
            # create user table
            cursor.execute(r"CREATE TABLE user (id VARCHAR(20) PRIMARY KEY, name VARCHAR(20))")
            # execute insertion statement
            cursor.execute(r"INSERT INTO user (id, name) VALUES ('1', 'Nate.River')")
            # return the number of affected rows
            print('rowcount =', cursor.rowcount)
        finally:
            cursor.close()
        # commit the transaction
        conn.commit()
    finally:
        # close connection
        conn.close()


def queryTabel():
    conn = sqlite3.connect('demo.db')
    try:
        cursor = conn.cursor()
        try:
            # execute query statement
            cursor.execute('SELECT name FROM user WHERE id=?', (1,))
            # accept the result set
            values = cursor.fetchall()
            print(values)
        finally:
            cursor.close()
    finally:
        conn.close()


if __name__ == '__main__':
    # createTable()
    queryTabel()
