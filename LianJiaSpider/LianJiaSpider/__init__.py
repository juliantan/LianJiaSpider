#_*_coding:utf-8_*_
import MySQLdb
import settings

settings.DB_Host = raw_input("Enter mysql host:")
settings.DB_Pwd = raw_input("3edcvgy7GLF")

conn = MySQLdb.connect(
	host=settings.DB_Host,
	user='root',
	passwd=settings.DB_Pwd)
dbName = "lianjiaspider"
tableName = "tb_newHouse"
cursor = conn.cursor()
status = cursor.execute("SELECT * FROM information_schema.schemata WHERE SCHEMA_NAME ='{0}'".format(dbName))#判断是否存在某数据库，存在status=1,不存在status=0
if status == 0:
	cursor.execute("CREATE DATABASE {0};use {0};CREATE TABLE {1}(ID INT PRIMARY KEY NOT null AUTO_INCREMENT,area VARCHAR(200),loupanName VARCHAR(200),address VARCHAR(200),doorModel VARCHAR(200),state VARCHAR(200),houseType VARCHAR(200),price VARCHAR(200),loupanurl VARCHAR(200));".format(dbName,tableName))
else:
	print "{0} is exists".format(dbName)
cursor.close()