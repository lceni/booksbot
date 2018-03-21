# -*- coding: utf-8 -*-
import scrapy


class BooksSpider(scrapy.Spider):
    name = "top-1m"

    start_urls = [
        'http://youtube.com/',
        'http://facebook.com/',
        'http://baidu.com/',
        'http://wikipedia.org/',
        'http://reddit.com/',
        'http://yahoo.com/',
        'http://qq.com/',
        'http://taobao.com/',
        'http://amazon.com/',
        'http://tmall.com/',
        'http://vk.com/',
        'http://twitter.com/',
        'http://instagram.com/',
        'http://sohu.com/',
        'http://sina.com.cn/',
        'http://live.com/',
        'http://jd.com/',
        'http://360.cn/',
        'http://weibo.com/',
        'http://yandex.ru/',
        'http://google.com.br/',
        'http://netflix.com/',
        'http://twitch.tv/',
        'http://login.tmall.com/',
        'http://alipay.com/',
        'http://yahoo.co.jp/',
        'http://bing.com/',
        'http://ebay.com/',
        'http://ok.ru/',
        'http://hao123.com/',
        'http://microsoft.com/',
        'http://t.co/',
        'http://imgur.com/',
        'http://wikia.com/',
        'http://mail.ru/',
        'http://imdb.com/'
    ]

    def parse(self, response):
        item = {}



        item['url'] = response.url
        item['title'] = response.css('title::text').extract_first()
        item['description'] = response.xpath("//meta[@name='description']/data(@content)").extract_first()
        item['keywords'] = response.xpath("//meta[@name='keywords']/data(@content)").extract_first()
        yield item

