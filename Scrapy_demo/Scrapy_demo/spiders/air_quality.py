# -*- coding: utf-8 -*-
import scrapy


class AirQualitySpider(scrapy.Spider):
    name = 'air_quality'
    allowed_domains = ['www.aqistudy.cn/historydata']
    start_urls = ['http://www.aqistudy.cn/historydata/']

    def parse(self, response):
        # 在请求完成时调用, response 是响应(请求返回来的). 
        """
        1. 解析响应(封装成 item 对象并返回 item 对象).
        2. 提取新的需要下载的 url, 创建新的 request 并返回.
        """
        city_list = response.xpath('//div[@class="all"]/div/li/a.text')
