#_*_coding:utf-8_*_
import MySQLdb

conn = MySQLdb.connect(
	host='localhost',
	user='root',
	passwd='123456')
dbName = "lianjiaspider"
tableName = "tb_newHouse"
cursor = conn.cursor()
status = cursor.execute("SELECT * FROM information_schema.schemata WHERE SCHEMA_NAME ='{0}'".format(dbName))#判断是否存在某数据库，存在status=1,不存在status=0
if status == 0:
	cursor.execute("CREATE DATABASE {0};use {0};CREATE TABLE {1}(ID INT PRIMARY KEY,area VARCHAR(200),loupanName VARCHAR(200),address VARCHAR(200),doorModel VARCHAR(200),state VARCHAR(200),houseType VARCHAR(200),price VARCHAR(200),areaurl VARCHAR(200));".format(dbName,tableName))
else:
	print "{0} is exists".format(dbName)
cursor.close()