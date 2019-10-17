"""信息爬虫基类
"""

import time
import random
import scrapy
import datetime
from selenium import webdriver

import laofan.utility as util
import laofan.settings as conf


class BaseParse(scrapy.Spider):
    name = 'BaseParse'
    domain = conf.DOMAIN

    def __init__(self, increment_low, increment_high):
        """解析器构造函数
        Args:
            increment_low  起始条目
            increment_high  终止条目
        """
        # 任务变量配置
        self.count = 0  # 每一轮已经完成的条目数
        self.current_item = 0  # 当前正在进行的条目
        self.increment_low = int(increment_low)
        self.increment_high = int(increment_high)
        self.all_items = self.increment_high - self.increment_low + 1
        self.mtva = conf.PREFIX_MAPS[self.name]
        
        # 时间变量配置
        self.yesterday = (datetime.datetime.now()-
            datetime.timedelta(days=1)).strftime("%m.%d")

        # 消息记录器配置
        record = util.Record(self.name)
        self.error = record.record_error  # 错误消息记录器
        self.console = record.record_console  # 控制台消息输出器

        # 下载器配置
        self.download = util.Download(self.mtva).download_image

        # chromedriver 配置
        self.options = webdriver.ChromeOptions()
        self.options.add_argument('--headless')
        self.options.add_argument('--no-sandbox')
        self.options.add_argument('--disable-dev-shm-usage')
        self.options.add_argument('--disable-gpu')
        self.options.add_argument('blink-conf=imagesEnabled=false')
        self.driver = webdriver.Chrome(
            conf.DRIVER_PATH, chrome_options=self.options)

    def check_update(self, response):
        try:
            result = response.xpath(conf.YUNBTV_UPDATE_TIME)[0].extract()
            if result == self.yesterday:
                return True
            print('\nignore...%s...\n' % response.url)
            return False
        except Exception:
            self.email("任务异常消息", "%s - 检查更新时间错误" % self.name)
            return False

    def extract_name(self, response):
        try:
            result = response.xpath(conf.YUNBTV_NAME)[0].extract()
            return result
        except Exception as e:
            self.error('extract_name', response.url, str(e))
            return conf.UNKNOW

    def extract_introduction(self, response):
        try:
            result = response.xpath(conf.YUNBTV_INTRODUCTION)[0].extract()
            result = result.replace("\"", "").replace("\'", "")
            return result
        except Exception as e:
            self.error('extract_introduction', response.url, str(e))
            return conf.UNKNOW

    def extract_director(self, response):
        try:
            result = response.xpath(conf.YUNBTV_DIRECTOR)[0].extract()
            result = result.replace("\"", "").replace("\'", "")
            return result
        except Exception as e:
            self.error('extract_director', response.url, str(e))
            return conf.UNKNOW

    def extract_actor(self, response):
        try:
            result = response.xpath(conf.YUNBTV_ACTOR).extract()
            if not len(result):
                return conf.UNKNOW
            actors = [actor.replace("\"", "").replace("\'", "")
                      for actor in result]
            str_actor = "、".join(actors)
            return str_actor
        except Exception as e:
            self.error('extract_actor', response.url, str(e))
            return conf.UNKNOW

    def extract_flag_time(self, response):
        try:
            result = response.xpath(conf.YUNBTV_FLAG_TIME)[0].extract()
            return result
        except Exception as e:
            self.error('extract_flag_time', response.url, str(e))
            return conf.UNKNOW

    def extract_flag_area(self, response):
        try:
            result = response.xpath(conf.YUNBTV_FLAG_AREA)[0].extract()
            return result
        except Exception as e:
            self.error('extract_flag_area', response.url, str(e))
            return conf.UNKNOW

    def extract_flag_type(self, response):
        try:
            result = response.xpath(conf.YUNBTV_FLAG_TYPE)[0].extract()
            return result
        except Exception as e:
            self.error('extract_flag_type', response.url, str(e))
            return conf.UNKNOW

    def extract_score(self, response):
        """ 影片得分采用随机数方式 """
        return round(random.uniform(8.0, 9.5), 1)

    def extract_img(self, response):
        try:
            result = response.xpath(conf.YUNBTV_URL_IMG)[0].extract()
            image_path = self.download(self.domain + result)
            if not image_path:
                raise Exception
            return image_path
        except Exception as e:
            self.error('extract_img', response.url, str(e))
            return conf.IMAGE_NOTFOUND_PATH

    def extract_update_time(self, response):
        return time.strftime("%Y-%m-%d", time.localtime())

    def extract_url(self, response):
        """提取视频播放的主页地址

            函数提取视频全部播放线路的地址，然后依次
        调用chrome_extract函数提取视频播放地址。
        """
        try:
            play_pages = response.xpath(conf.YUNBTV_MOVIE_LINK).extract()
            for play_page in play_pages:
                play_address = self.chrome_extract(
                    "%s%s" % (self.domain, play_page))
                # 如果解析后地址后缀名不是m3u8，说明这个地址是无效的，应舍弃
                if(play_address.split('.')[-1] == 'm3u8'):
                    return play_address.replace(conf.DEL_PREFIX,'')
            return conf.PLAY_INVALID_PATH
        except Exception as e:
            self.error('extract_url', response.url, str(e))
            return conf.PLAY_INVALID_PATH

    def extract_urls(self, response):
        """提取剧集播放的主页地址

            电视剧、综艺、动漫等会包含很多剧集，函数提取每一个
        剧集播放的主页地址并依次调用chrome_extract函数提取视
        频播放地址。
        """
        play_addresses = []
        try:
            play_pages = response.xpath(conf.YUNBTV_EPISODE_LINK).extract()
            nums = len(play_pages)  # 全部剧集数
            current = 1  # 当前解析的剧集
            print("\n\n开始解析剧集播放地址，共 %s 集" % nums)

            for play_page in play_pages:
                self.console("当前剧集 %d " % current, nums, current)
                play_address = self.chrome_extract(
                    "%s%s" % (self.domain, play_page))
                play_addresses.append(play_address.replace(conf.DEL_PREFIX,''))
                current = current + 1
                self.count = self.count + 1

        except Exception as e:
            self.error('extract_url', response.url, str(e))
        return play_addresses

    def chrome_extract(self, play_page):
        """提取播放地址

            函数加载视频播放的主页地址，并提取HTML中iframe
        标签的属性src，src属性值即为播放地址；
            由于iframe框架是加载完视频播放的主页地址后由JS动态
        生成的，而传统的信息解析方式不能执行JS脚本，所以这里采用
        浏览器获取页面并执行JS脚本，再去解析视频真正的播放地址。
        """
        try:
            self.driver.get(play_page)
            iframe = self.driver.find_elements_by_tag_name('iframe')[0]
            play_address = iframe.get_attribute('src')
            return play_address
        except Exception as e:
            self.error('chrome_extract', '', str(e))
            return ""

    def extract_mtva(self, response):
        return self.mtva

    def check(self):
        """每解析完成一个条目，便执行一次check函数；
        check函数执行与任务相关的检查，这些检查包含：

        1. 判断当前已经解析完完成的条目数量是否超过
        自定义的每轮最大解析次数，若超过则重置webdriver
        2. 判断全部的条目是否都已经解析完毕，若全部的
        条目都已经解析完毕，则调用task_completed函数
        """
        if (self.count >= conf.MAX_CRAWL_NUMS):
            self.count = 0
            self.restart_driver()
        if self.current_item == self.all_items:
            self.task_completed()

    def restart_driver(self):
        """长时间的运行会导致浏览器驱动程序占用越来越多的
        内存，为防止内存占用过大，需要间隔一段时间重启浏览器
        """
        self.driver.quit()
        self.driver = webdriver.Chrome(
            conf.DRIVER_PATH, chrome_options=self.options)

    def task_completed(self):
        """任务完成后要执行的函数
           函数退出浏览器驱动程序
        """
        self.driver.quit()
