# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import time
import MySQLdb

class LianjiaspiderPipeline(object):
    def process_item(self, item, spider):

        conn = MySQLdb.connect(
            host='localhost',
            port=3306,
            user='root',
            passwd='123456',
            db='ljspider',
            charset='utf8'
        )
        cur = conn.cursor()

        cur.execute("insert into tb_lj(loupanName,address,doorModel,state,houseType,price) values(%s,%s,%s,%s,%s,%s)",(item['loupanName'][0].encode('utf8'), item['address'][0].encode('utf8'),item['doorModel'][0].encode('utf8'),item['state'][0].encode('utf8'), item['houseType'][0].encode('utf8'), item['price'][0].encode('utf8')))


        # now = time.strftime('%Y-%m-%d', time.localtime())
        # fileName = u'链家' + now + '.txt'
        # with open(fileName, 'a') as fp:
        #     fp.write(item['loupanName'][0].encode('utf8') + '\n')
        #     fp.write(item['address'][0].encode('utf8') + '\n')
        #     fp.write(item['doorModel'][0].encode('utf8') + '\n')
        #     fp.write(item['state'][0].encode('utf8') + '\n\n')
        #     fp.write(item['houseType'][0].encode('utf8') + '\n')
        #     fp.write(item['price'][0].encode('utf8') + '\n\n')

        cur.close()
        conn.commit()
        conn.close()

        return item
