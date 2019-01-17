# -*- coding: utf-8 -*-
import pymysql
# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html


class GamePipeline(object):
    def process_item(self, item, spider):
        conn=pymysql.connect(host='127.0.0.1',user='root',passwd='967100',db='python',charset='utf8')
        try:
            for i in range(0,len(item['title'])):
                title=item['title'][i]
                entitle=item['entitle'][i]
                time=item['time'][i]
                lan=item['lan'][i]
                type=item['type'][i]
                pc=item['pc'] [i]
                num=item['num'][i]
                with conn.cursor() as cursor:
                    sql="insert into 3dmgame(title,entitle,num,time,lan,type,pc) values('"+ title +"','" + entitle + "','" + num +"','"+ time +"','"+ lan +"','"+ type +"','"+ pc +"')"
                    try:
                        cursor.execute(sql)
                    except Exception as err:
                        print(err)
                conn.commit()
            conn.close()
        except Exception as err:
            print(err)
        return item
