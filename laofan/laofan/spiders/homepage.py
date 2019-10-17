"""主页地址爬虫
"""

import json
import scrapy

import laofan.utility as util
import laofan.settings as conf
import laofan.merlist as merge


class Homepage(scrapy.Spider):
    name = "Homepage"
    domain = conf.DOMAIN

    def __init__(self, start_url=None,
                 increment_low=0, increment_high=0,
                 video_type=None):
        """
        Args:
            start_url 起始地址
            increment_low 起始条目
            increment_high 终止条目
            video_type 视频类型
        """
        self._url = start_url
        self._current_item = int(increment_low)  # 当前条目
        self._increment_low = int(increment_low)
        self._increment_high = int(increment_high)
        self._video_type = video_type
        self._homepage_tpl = conf.HOMEPAGE_MAPS[video_type]

        # 消息记录器配置
        record = util.Record(self._video_type)
        self._error = record.record_error  # 错误消息记录器
        self._console = record.record_console  # 控制台消息输出器

    def start_requests(self):
        yield scrapy.Request(self._url, callback=self.parse)

    def parse(self, response):
        """函数负责视频主页的解析，每个目标地址下有N个主页地址
        该函数以N个地址为一个单位，将这些地址存储到本地磁盘中去
        """
        try:
            pages = response.xpath(conf.YUNBTV_HOMEPAGE).extract()
            page_list = ["%s%s" % (self.domain, page) for page in pages]

            # 存储URL到本地磁盘
            file_dir = 'tmp/%s/' % self._video_type
            file_name = '%d.json' % self._current_item
            with open("%s%s" % (file_dir, file_name), "w") as f:
                json.dump(page_list, f)

        except Exception as e:
            self.error('extract_homepage', self._url, str(e))
        self._console(self._url, self._increment_high, self._current_item)

        self._current_item = self._current_item + 1
        if(self._current_item <= self._increment_high):  # 任务未完成
            self._url = self._homepage_tpl % self._current_item
            yield scrapy.Request(self._url, callback=self.parse)
        else:  # 任务已经完成
            self._task_completed()

    def _task_completed(self):
        """任务结束后要执行的函数；函数调用
        merlist模块下的comerge函数完成URL的合并
        """
        merge.comerge(self._video_type, self._increment_low,
                      self._increment_high)
