# -*- coding: utf-8 -*-
import scrapy


class NaverbikeSpider(scrapy.Spider):
    name = 'naverbike'
    allowed_domains = ['auto.naver.com/bike/mainList.nhn']
    start_urls = ['http://auto.naver.com/bike/mainList.nhn']

    def parse(self, response):
        print(response.text)
        # pass
