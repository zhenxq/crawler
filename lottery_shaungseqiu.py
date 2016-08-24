# coding:utf-8

import  requests
from bs4 import BeautifulSoup
import re
import csv

def welfareLotteries(result_write,url):
    print url
    r = requests.get(url)
    soup = BeautifulSoup(r.content,"lxml")
    for table_item in soup.find("table",bordercolor="#CC6600"):
        if table_item != "\n":
            for tr_item in  table_item.find_all("tr"):
                if tr_item.find(height="35"):
                    data_time_num = tr_item.find(height="35").text
                    num = ""
                    for num_item in tr_item.find_all("span"):
                        num += num_item.text.strip()
                    first_prize_num = tr_item.find(text=re.compile(u"注")).replace(u"注", "")
                    money_item = tr_item.find_all(text=re.compile(u"元"))
                    consumption_sum = money_item[0]
                    prize_pool = money_item[1]
                    result_write.writerow( [data_time_num.encode("utf-8"), num.encode("utf-8"), first_prize_num.encode("utf-8"), consumption_sum.encode("utf-8"), prize_pool.encode("utf-8")])


def main(result_file):
    with open(result_file,"w") as csvfile:
        result_write  = csv.writer(csvfile)
        for i in range(28):
            if i != 0:
                url = "http://www.cwl.gov.cn/kjxx/ssq/hmhz/index_%d.shtml"%i
            else:
                url = "http://www.cwl.gov.cn/kjxx/ssq/hmhz/index.shtml"
            welfareLotteries(result_write,url)

if __name__ == "__main__":
    result_file = "shuangseqiu.csv"
    main(result_file)