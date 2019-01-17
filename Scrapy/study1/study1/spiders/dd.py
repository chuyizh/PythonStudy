# -*- coding: utf-8 -*-
import scrapy
from study1.items import Study1Item
from scrapy.http import Request
import re

class DdSpider(scrapy.Spider):
    name = 'dd'
    allowed_domains = ['dangdang.com']
    start_urls = ['http://search.dangdang.com/?key=%C5%A3%D7%D0%BF%E3&page_index=1']

    def parse(self, response):
        item=Study1Item()
        item['title']=response.xpath('//a[@name="itemlist-picture"]/@title').extract()
        item['link']=response.xpath('//a[@name="itemlist-picture"]/@href').extract()
        item['comment']=response.xpath('//a[@name="itemlist-review"]/text()').extract()
        item['price']=response.xpath('//span[@class="price_n"]/text()').re('&yen;(.*?)')
        item['dpname'] = response.xpath('//a[@name="itemlist-shop-name"]/@title').extract()
        yield item
        for i in range(2,80):
            url='http://search.dangdang.com/?key=%C5%A3%D7%D0%BF%E3&page_index='+str(i)
            yield Request(url,callback=self.parse)