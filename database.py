import sqlite3

# # create database
# conn = sqlite3.connect('users.db')

# print("Opened database successfully")


# create table
conn = sqlite3.connect('users.db')

# conn.execute('''CREATE TABLE COMPANY
#          (ID INTEGER PRIMARY KEY     AUTOINCREMENT,
#          NAME           TEXT    NOT NULL,
#          EMAIL           TEXT     NOT NULL,
#          MOBILE        CHAR(50),
#          PASSWORD         CHAR(20));''')

conn.execute('''CREATE TABLE Employee
         (ID INTEGER PRIMARY KEY     AUTOINCREMENT,
         NAME           TEXT    NOT NULL,
         EMAIL           TEXT     NOT NULL,
         MOBILE        CHAR(50),
         AGE            INTEGER,
         ADDRESS        TEXT     NOT NULL,
         GENDER         CHAR(50),
         JOINING_DATE   CHAR(50));''')
print("Table created successfully")

conn.close()