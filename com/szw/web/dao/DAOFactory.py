#!/usr/bin/env python
# encoding: utf-8

"""
@author: WillSo
@license: Apache Licence 
@software: PyCharm
@file: DAOFactory.py
@time: 2017\10\16 0016 15:26
"""

from com.szw.web.bean import Bean
import sqlite3

User = Bean.User

def connect_db() :
    rv = sqlite3.connect('./db.sqlite3')
    # rv.row_factory = sqlite3.Row
    return rv

class UserDAO:
    def __init__(self):
        self.conn = connect_db()
        self.cursor = self.conn.cursor()

    def insert(self, user):
        try :
            sql = "insert into '%s' values ('%s', '%s')" % ('user', user.get_id(), user.get_name())
            self.cursor.execute(sql)
            self.conn.commit()
            return True
        except:
            print('ERROR')
        finally:
            self.close(self.cursor, self.conn)

    def queryAll(self):
        try:
            sql = "select * from '%s'" % ('user')
            self.cursor.execute(sql)
            value = self.cursor.fetchall()
            return value
        except:
            print('ERROR')
        finally:
             self.close(self.cursor, self.conn)

    def close(self, cursor, conn):
        cursor.close()
        conn.close()

class DAOFactory:
    @staticmethod
    def getDAOImpl(name):
        return {
            User.__name__ : UserDAO()
        }.get(name)

if __name__ == '__main__':
    pass