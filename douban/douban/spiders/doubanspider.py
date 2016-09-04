#coding:utf-8

from scrapy.contrib.spiders import CrawlSpider
from scrapy.http import Request
# from scrapy.selector import Selector           #1：可以使用scrapy自带的Selector；2：使用lXMl/Bs4；3：直接用response来解析。
from douban.items import DoubanItem              #items.py文件中类

class Douban(CrawlSpider):
    name = "doubanTest"
    start_urls = ["http://movie.douban.com/top250"]#根据起始url创建Request对象,并将parse方法作为回调函数。
    url = "http://movie.douban.com/top250"         #用于合成下一页完整链接的url
    def parse(self, response):					   #Request对象经过调度，执行生成 scrapy.http.Response 对象并送回给spider parse() 方法。
        # print response.body
        # print response.url
        # response.xpath()
        Items = DoubanItem()
        # selector = Selector(response)
        # movie_info = selector.xpath('//div[@class="info"]')
        movie_info = response.xpath('//div[@class="info"]')
        for info_item in movie_info:
            title = info_item.xpath('div[@class="hd"]/a/span/text()').extract()
            title = "".join(title)
            intro = info_item.xpath('div[@class="bd"]/p/text()').extract()
            intro = ";".join(intro).strip()
            star = info_item.xpath('div[@class="bd"]/div[@class="star"]/span[@class="rating_num"]/text()').extract()[0]
            quote = info_item.xpath('div[@class="bd"]/p[@class="quote"]/span/text()').extract()
            quote = quote[0] if quote else ""
            Items["title"] = title
            Items["intro"] = intro
            Items["star"] = star
            Items["quote"] = quote
            yield Items                            #通过生成器将信息传出去到items.py,然后根据settings.py的配置，就会生成csv文件
        # next_link = selector.xpath('//span[@class="next"]/link/@href').extract()
        next_link = response.xpath('//span[@class="next"]/link/@href').extract()
        if next_link:
            next_link = self.url + next_link[0]
            print next_link
            yield Request(next_link,callback=self.parse)#将新的url传递构建的Request 对象，重新回掉parse