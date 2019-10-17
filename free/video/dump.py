import time
import redis
from video.config import email
from video.models import Ranking
from video.config import redis_pool


class RedisDump(object):
    def __init__(self):
        self._pool = redis_pool

    def dump(self):
        today = time.localtime()[2]  # 几天是几号
        r = redis.Redis(connection_pool = self._pool)
        keys = r.keys()
        values = r.mget(keys)

        try:
            for key,value in zip(keys, values):
                rank = Ranking.objects.get(vid = key.decode())
                rank.rday = int(value.decode())
                rank.rweek = rank.rweek + rank.rday
                rank.rmonth = rank.rmonth + rank.rday
                if today == 1:
                    rank.rmonth = 0
                if today % 7 == 0:
                    rank.rweek = 0    
                rank.save()
            r.flushdb()
            return True
        except Exception as e:
            email.send("DUMP数据库出错", str(e))
            return False
