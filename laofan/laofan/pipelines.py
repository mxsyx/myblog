"""数据存储管道
"""

import time
import scrapy

import laofan.utility as util
import laofan.settings as conf
from laofan.database import Database


class BasePipeline(object):
    def __init__(self, pipeline_name, video_type):
        """ 基类构造函数
        arguments:
            pipeline_name 管道名
            video_type 视频类型名
        """
        self.db = Database()  # 数据库访问对象
        self.record = util.Record(pipeline_name)
        self.video_type = video_type
        self.prefix = conf.PREFIX_MAPS[video_type]

    def get_maxid(self):
        """获取数据表中最大的ID,当数据表中无数据时
        MySQLDB将返回None,此时需要将maxid设置为0
        """
        maxid = None
        statement = conf.STATEMENT['GET_MAXID']
        arguments = (self.video_type)
        if self.db.execute_query(statement, arguments):
            maxid = self.db.fetch_queryone()
        if not maxid:
            return 0
        return maxid

    def get_videoid(self, video_name):
        """根据视频的名字获取视频的ID"""
        video_id = None
        statement = conf.STATEMENT['GET_VIDEOID']
        arguments = (self.video_type, video_name)
        if self.db.execute_query(statement, arguments):
            video_id = self.db.fetch_queryone()
        if not video_id:
            return 0
        return video_id

    def update_ranking(self, maxid):
        """向排行数据表中新增一条数据，当插入的
        数据与数据表中的数据冲突时则不插入这条数据"
        """
        if maxid == self.get_maxid():  # 说明不久前新增了数据
            statement = conf.STATEMENT['UPDATE_RANKING']
            arguments = (self.prefix, maxid)
            return self.db.execute_update(statement, arguments)
        return True

    def update_urls(self, urls, video_id):
        """将剧集的播放地址按顺序存储到数据库中"""
        statement = conf.STATEMENT['UPDATE_URLS']
        arguments = [(self.video_type, video_id, i+1, urls[i], urls[i])
                     for i in range(0, len(urls))]
        return self.db.execute_many(statement, arguments)

    def record_info(self, video_name):
        """记录一条成功完成存储的消息"""
        self.record.record_info("更新存储成功：%s" % video_name)


class MoviePipeline(BasePipeline):
    def __init__(self):
        super(MoviePipeline, self).__init__(
            'MoviePipeline', 'movie')

    def process_item(self, item, spider):
        if(item['mtva'] != 'm'):
            return item
        self.update_item(item)
        return item

    def update_item(self, item):
        maxid = self.get_maxid() + 1
        values = [maxid]
        values.extend(list(item.values())[0:11])
        values.extend(list(item.values())[9:11])

        statement = conf.STATEMENT['UPDATE_MOVIE']
        if self.db.execute_update(statement, tuple(values)):
            if self.update_ranking(maxid):
                if self.db.execute_commit():
                    self.record_info(item['name'])


class TvseriesPipeline(BasePipeline):
    def __init__(self):
        super(TvseriesPipeline, self).__init__(
            'TvseriesPipeline', 'tvseries')

    def process_item(self, item, spider):
        if(item['mtva'] != 't'):
            return item
        self.update_item(item)
        return item

    def update_item(self, item):
        maxid = self.get_maxid() + 1

        values = [maxid]
        values.extend(list(item.values())[0:10])
        values.extend(list(item.values())[9:10])
        statement = conf.STATEMENT['UPDATE_TVSERIES']
        if self.db.execute_update(statement, tuple(values)):
            if self.update_ranking(maxid):
                self.update_url(item)

    def update_url(self, item):
        urls = item['urls']
        video_id = self.get_videoid(item['name'])
        if self.update_urls(urls, video_id):
            if self.db.execute_commit():
                self.record_info(item['name'])


class VarietyPipeline(BasePipeline):
    def __init__(self):
        super(VarietyPipeline, self).__init__(
            'VarietyPipeline', 'variety')

    def process_item(self, item, spider):
        if(item['mtva'] != 'v'):
            return item
        self.update_item(item)
        return item

    def update_item(self, item):
        maxid = self.get_maxid() + 1

        values = [maxid]
        values.extend(list(item.values())[0:10])
        values.extend(list(item.values())[9:10])
        statement = conf.STATEMENT['UPDATE_VARIETY']

        if self.db.execute_update(statement, tuple(values)):
            if self.update_ranking(maxid):
                self.update_url(item)

    def update_url(self, item):
        urls = item['urls']
        video_id = self.get_videoid(item['name'])
        if self.update_urls(urls, video_id):
            if self.db.execute_commit():
                self.record_info(item['name'])


class AnimePipeline(BasePipeline):
    def __init__(self):
        super(AnimePipeline, self).__init__(
            'AnimePipeline', 'anime')

    def process_item(self, item, spider):
        if(item['mtva'] != 'a'):
            return item
        self.update_item(item)
        return item

    def update_item(self, item):
        maxid = self.get_maxid() + 1

        values = [maxid]
        values.extend(list(item.values())[0:10])
        values.extend(list(item.values())[9:10])
        statement = conf.STATEMENT['UPDATE_ANIME']

        if self.db.execute_update(statement, tuple(values)):
            if self.update_ranking(maxid):
                self.update_url(item)

    def update_url(self, item):
        urls = item['urls']
        video_id = self.get_videoid(item['name'])
        if self.update_urls(urls, video_id):
            if self.db.execute_commit():
                    self.record_info(item['name'])
