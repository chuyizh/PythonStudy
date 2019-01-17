# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class Study1Pipeline(object):
    def process_item(self, item, spider):
        conn=pymysql.connect(host='localhost',user='root',password='967100',db='python',charset='utf8')
        for i in range(0,len(item['title'])):
            title=item['title'][i]
            dpname=item['dpname'][i]
            #price=item['price'][i]
            comment=item['comment'][i]
            link = item['link'][i]
            with conn.cursor() as cursor:
                sql = "insert into dangdang(title,dpname,commentdata,link) values('" + title + "','" + dpname + "','" + comment + "','" + link + "')"
                #sql = "insert into dangtest(title,dpname,price,commentdata,link) values('" + title + "','" + dpname + "','" + price + "','" + comment + "','" + link + "')"
                try:
                    cursor.execute(sql)
                except Exception as err:
                    print(err)
            conn.commit()

        conn.close()
        return item
