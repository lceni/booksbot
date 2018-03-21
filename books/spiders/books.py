# -*- coding: utf-8 -*-
import scrapy
import zipfile
import csv
import os

class BooksSpider(scrapy.Spider):
    name = "top-1m"

    start_urls = []

    def start_requests(self):
        print os.path.abspath(os.path.dirname(__file__))

        zipFile = zipfile.ZipFile(os.path.abspath(os.path.dirname(__file__)) + '/top-1m.csv.zip')
        csvFile = zipFile.open('top-1m.csv')
        spamReader = csv.reader(csvFile, delimiter=',')
        for row in spamReader:
            yield scrapy.Request(row[1], self.parse)



    def parse(self, response):
        item = {}
        item['url'] = response.url
        item['title'] = response.css('title::text').extract_first()
        item['description'] = response.xpath("//meta[@name='description']/@content").extract_first()
        item['keywords'] = response.xpath("//meta[@name='keywords']/@content").extract_first()
        yield item

