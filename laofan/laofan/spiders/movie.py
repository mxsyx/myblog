"""电影信息爬虫
"""

import json
import scrapy

import laofan.settings as conf
from laofan.base import BaseParse
from laofan.items import MovieItem


class MovieParse(BaseParse):
    name = 'MovieParse'

    def __init__(self, increment_low=0, increment_high=0):
        super(MovieParse, self).__init__(increment_low, increment_high)

    def start_requests(self):
        """函数从movie.new.json文件中
        获取URL以逐条解析数据，返回一个迭代器
        """
        with open(conf.URL_FILE_PATH_M, 'r') as url_file:
            url_list = json.load(url_file)
            for i in range(self.increment_low, self.increment_high + 1):
                yield scrapy.Request(url_list[i-1], callback=self.parse)

    def parse(self, response):
        """电影信息解析

            parse函数负责解析电影主页中的信息，将与此电影有关的信息例如名字、
        简介、年代、播放地址等信息提取出来封装到 MovieItem 类中，并将结果传
        送到存储器pipelines
            每条电影信息都有一个对应的函数负责提取，这些函数以extract_开头
        """
        item = MovieItem()
        if not self.check_update(response):
            return None
        item['name'] = self.extract_name(response)
        item['introduction'] = self.extract_introduction(response)
        item['director'] = self.extract_director(response)
        item['actor'] = self.extract_actor(response)
        item['flag_time'] = self.extract_flag_time(response)
        item['flag_area'] = self.extract_flag_area(response)
        item['flag_type'] = self.extract_flag_type(response)
        item['score'] = self.extract_score(response)
        item['url_img'] = self.extract_img(response)
        item['update_time'] = self.extract_update_time(response)
        item['url'] = self.extract_url(response)
        item['mtva'] = self.extract_mtva(response)
        
        self.count = self.count + 1
        self.current_item = self.current_item + 1
        self.console(response.url, self.all_items, self.current_item)
        
        self.check()

        yield item
