#coding:utf-8
from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import Request
from daomubiji.items import DaomubijiItem

class DaoMuBiGi(CrawlSpider):
    name = "daomubiji"
    start_urls = ["http://www.daomubiji.com/"]
    def parse(self, response):
        book_list= response.xpath("//table")
        for book_item in book_list:
            book_name = book_item.xpath(".//center/h2/text()").extract()[0]
            capture_list = book_item.xpath(".//tr/td/a")
            for capture_item in capture_list:
                Items = DaomubijiItem()
                capture_name = capture_item.xpath("text()").extract()[0]
                caputre_url =  capture_item.xpath("@href").extract()[0]
                Items["book_name"] = book_name
                Items["capture_name"] = capture_name
                Items["caputre_url"] = caputre_url
                yield Items
