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

        cur.execute("insert into tb_lj(area,loupanName,address,doorModel,state,houseType,price,loupanurl) values(%s,%s,%s,%s,%s,%s,%s,%s)",(
            item['area'][0].encode('utf8').replace('楼盘',''),
            item['loupanName'][0].encode('utf8'),
            item['address'][0].encode('utf8'),
            item['doorModel'][0].encode('utf8').replace('\r','').replace('\n','').replace('\t','').replace(' ',''),
            item['state'][0].encode('utf8'),
            item['houseType'][0].encode('utf8'),
            item['price'][0].encode('utf8').replace('\r','').replace('\n','').replace('\t','').replace(' ',''),
            item['areaurl'][0].encode('utf8') + item['loupanurl'][0].encode('utf8')[1:]))


        # now = time.strftime('%Y-%m-%d', time.localtime())
        # fileName = u'链家' + now + '.txt'
        # with open(fileName, 'a') as fp:
        #     fp.write(item['area'][0].encode('utf8')+'\n')
        #     fp.write(item['loupanName'][0].encode('utf8') + '\n')
        #     fp.write(item['address'][0].encode('utf8') + '\n')
        #     fp.write(item['doorModel'][0].encode('utf8').replace('\r','').replace('\n','').replace('\t','').replace(' ','') + '\n')
        #     fp.write(item['state'][0].encode('utf8') + '\n\n')
        #     fp.write(item['houseType'][0].encode('utf8') + '\n')
        #     fp.write(item['price'][0].encode('utf8') + '\n\n')
        #     fp.write(item['areaurl'][0].encode('utf8') + item['loupanurl'][0].encode('utf8') + '\n\n')

        cur.close()
        conn.commit()
        conn.close()

        return item
