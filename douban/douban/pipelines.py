# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html

#处理从items.py中收集的字段数据。
#可以在settings.py中设置ITEM_PIPELINES = {'工程文件名.pipelines.DoubanPipeline':300,}来启动pipelines中的相应方法，以及相应方法的优先级。
#The integer values you assign to classes in this setting determine the order in which they run: items go through from lower valued to higher valued classes. It’s customary to define these numbers in the 0-1000 range.

class DoubanPipeline(object):
    def process_item(self, item, spider):#item数据是从items.py传递过来的
        return item
        #这个方法必须返回一个 Item (或任何继承类)对象
		#使用return item或是抛出 rais DropItem("Missing price in %s" % item)
    def open_spider(self,spider):
        pass
    def close_spider(self,spider):
        pass