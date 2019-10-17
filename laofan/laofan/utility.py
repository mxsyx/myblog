import os
import time
import requests

from laofan import emails
import laofan.settings as conf

class Record(object):
    def __init__(self, name):
        self._name = name  # 爬虫名
        self._errors = 0  # 错误数量
        
    def record_error(self, where='', url='', info=''):
        """记录错误消息

        每记录一次错误消息，错误数量self._errors
        便自增1,这个错误数量最终要随邮件发送给管理员
        Args:
            where 出错时的位置
            url   出错时的地址
            info  错误消息
        """
        conf.logerr.error("In %s.%s  URL: %s \nException: %s\n" %
                          (self._name, where, url, info))
        self._errors = self._errors + 1

    def record_info(self, info):
        """记录提示消息

        Args:
            info 提示消息
        """
        conf.loginfo.info("In %s - %s" % (self._name, info))

    def record_console(self, url='', all_items=0, current_item=0):
        """控制台消息输出

           函数向控制台打印一条消息，通常该消息指示一个条目已经
        抓取完成，仅在CONSOLE_STATUS为True的情况下才打印消息
        Args:
            url 当前抓取的URL
            all_items 全部的条目数
            current_item 当前条目
        """
        if conf.CONSOLE_STATUS:
            print("\n解析成功 %s  > > > 剩余 %d 条\n" %
                  (url, all_items - current_item))


class Download(object):
    def __init__(self, mtva):
        self._mtva = mtva

    def download_image(self, img_url):
        """下载图片并保存到磁盘

        Args:
            img_url 图片地址
        函数返回图片在本机上的地址
        """
        # 图片名字为当前时间戳字符串
        img_name = "%d.jpg" % int(time.time()*1000000)
        img_dir = "img%s/%s/" % (
            self._mtva, time.strftime("%Y-%m-%d", time.localtime()))
        img_path = "%s%s" % (img_dir, img_name)

        # 存放图片的目录不存在时新建目录
        if not os.path.isdir(img_dir):
            os.mkdir(img_dir)

        try:
            image = requests.get(img_url)
            # 若图片小于1kb，说明图片已经损坏，应舍弃这张图片
            if int(image.headers['Content-Length']) < 1000:
                return conf.IMAGE_NOTFOUND_PATH
            # 将图片存储到本地磁盘上
            with open(img_path, 'wb') as f:
                f.write(image.content)
            return "/media/%s" % img_path
        except Exception:
            return False
