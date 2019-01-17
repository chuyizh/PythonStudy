# -*- coding: utf-8 -*-
import scrapy
from scrapy.http import Request
from game.items  import GameItem

class A3dmSpider(scrapy.Spider):
    name = '3dm'
    allowed_domains = ['3dmgame.com']
    start_urls = ['https://www.3dmgame.com/phb.html','https://www.3dmgame.com/qidaiphb.html','https://ww w.3dmgame.com/2018phb.html','https://www.3dmgame.com/2017phb.html']

    def parse(self, response):
        item = GameItem()
        item['title']=response.xpath('//div[@class="bt"]//a/text()').extract()
        item['entitle'] =response.xpath('//div[@class="bt"]//span/text()').extract()
        item['time'] =response.xpath('//ul[@class="infolis"]//li[3]/text()').extract()
        item['lan'] =response.xpath('//ul[@class="infolis"]//li[6]/text()').extract()
        item['type'] =response.xpath('//ul[@class="infolis"]//li[4]/text()').extract()
        item['pc']=response.xpath('//ul[@class="infolis"]//li[5]/text()').extract()
        item['num'] =response.xpath('//div[@class="num"]/text()').extract()
        yield item

