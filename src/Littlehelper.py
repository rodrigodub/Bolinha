#! /usr/bin/python3

#################################################
#                   Littlehelper
# Little Helper is just an utility module for
# database and text methods
#
# v0.1.004
# Issue #3
#
# Rodrigo Nobrega
# 20150713-
#################################################
__author__ = 'Rodrigo Nobrega'

# import modules
import pypyodbc
import sqlite3


# LHAuthenticate() was developed as Godzilla.GzAuthenticate()
# to get username and password to connect to Jira
class LHAuthenticate(object):
    def __init__(self):
        self.username = input('Username: ')
        self.pwd = input('Password: ')


# Class LHQuery() aggregates all functions to query the databases.
# Inherited, reused/modified from:
# Godzilla.GzQuery(),
# Difool.DfPersistence(),
# Snoopy.SnDatabaseFunctions()
class LHQuery(object):
    """
    LHQuery aggregate a number of functions to connect, query,
    and insert data into a database
    --
    TO DO: covnvert connection strings, query_db() and insert_db()
    to be used as generic
    """
    def __init__(self, user=None, pwd=None):
        self.dbCRM = r'DRIVER={SQL Server};SERVER=CROWN\PIVOTAL;DATABASE=ProductionED;Trusted_Connection=yes'
        self.dbJira = r'DRIVER=SQL Server;SERVER=JIRA;UID={};PWD={};' \
                      r'DATABASE=jiradb;Trusted_Connection=no'.format(user, pwd)
        self.dbSQLite = 'persistence.sqlite3'

    def query_db(self, mode, query, args=()):
        """
        Queries the database.
        mode: 'SQLite3' or 'SQL Server'
        query: SQL expression - strings to be replaced at ?, ?, etc
        args: strings to replace the question marks (note: finally implemented)
        """
        if mode == 'Jira':
            conn = pypyodbc.connect(self.dbJira)
        elif mode == 'CRM':
            conn = pypyodbc.connect(self.dbCRM)
        elif mode == 'SQLite3':
            conn = sqlite3.connect(self.dbSQLite)
        else:
            conn = None
        cur = conn.cursor()
        cur.execute(query, args)
        rv = cur.fetchall()
        cur.close()
        conn.commit()
        return rv

    def insert_db(self, mode, query, args=()):
        """
        Inserts into the database.
        mode: 'SQLite3' or 'SQL Server'
        query: SQL expression - strings to be replaced at ?, ?, etc
        args: strings to replace the question marks
        """
        if mode == 'Jira':
            conn = pypyodbc.connect(self.dbJira)
        elif mode == 'CRM':
            conn = pypyodbc.connect(self.dbCRM)
        elif mode == 'SQLite3':
            conn = sqlite3.connect(self.dbSQLite)
        else:
            conn = None
        c = conn.cursor()
        c.execute(query, args)
        conn.commit()
        return True


# LHFile
# reused from Difool.DfLogFile()
class LHFile(object):
    """
    DfLogFile opens a file, appends new info at the end, and closes it.
        Modified on v0.1.0810 to receive the filename when instantiated
    """
    def __init__(self, file):
        """
        :param file: string     - the log file, usually declared as variable LOGFILE
        """
        self.file = r'{}'.format(file)

    def writeInfo(self, param):
        """
        Method to open a file in Append mode, write the argument passed as param,
        add a new line, and close the file for writing.
        :param param: string    - what to write to the log file
        """
        # open file in Append mode
        f = open(self.file, 'a')
        # write to file the argument param, and a new line
        f.write(param)
        f.write('\n')
        # close the file
        f.close()

    def readInfo(self):
        """
        Method to scan the file, returns a list
        """
        arq = open(self.file, 'r')
        result = []
        #arq.readline()
        [result.append(i) for i in arq]
        arq.close()
        return result


# test loop
def test():
    print('------------------------')
    print('Test.')
    print('------------------------')


# main loop
def main():
    print('------------------------')
    print('Main.')
    print('------------------------')


# main, calling main loop
if __name__ == '__main__':
    test()
    # main()
