""" URL管理器

    tmp目录下有两种类型的url文件，xx.new.json, xx.all.json
    xx.new.json：存储计划任务中的URL
    xx.all.json：存储某个站点全部的URL
"""

import os
import sys
import json
import shutil


def merge_urls(ldir, low, high):
    """合并URL到一个文件

    返回值：
        url_list 合并后的URL列表
    """
    url_list = []
    for i in range(int(low), int(high)+1):
        with open("tmp/%s/%d.json" % (ldir, i), 'r') as f:
            url_list.extend(json.load(f))
    return url_list


def extend_urls(ldir, url_list):
    """将最新的URL扩展到xx.all.json

    Args:
        url_list 合并后的URL列表
    """
    with open("tmp/%s.all.json" % ldir, "r+") as file:
        urls_tmp = set(url_list)
        urls_all = set(json.load(file))
        urls_extend = list(urls_tmp | urls_all)
        file.seek(0)
        file.truncate()
        json.dump(urls_extend, file)


def comerge(ldir, low, high):
    """合并与扩展URL

    Args:
        ldir 存储URL文件的目录
        low  起始URL文件的编号
        high 终止URL文件的编号
    """
    url_list = merge_urls(ldir, low, high)
    with open("tmp/%s.new.json" % ldir, "w") as f:
        json.dump(url_list, f)
    extend_urls(ldir, url_list)
