import time
import redis
import random
from video.config import email
from video.config import SWITCH
from video.models import Feedback
from video.config import redis_pool


def add_play_volume(video_type, video_id):
	"""增加某个视频的播放量

	用户每点击一次播放按钮，
	便向REDIS数据库更新某个视频的播放量。
	Args:
		video_type 视频类型前缀
		video_id 视频ID
	"""
	try:
		r = redis.Redis(connection_pool=redis_pool)
		r.incr("%s_%d" % (video_type, video_id))
	except Exception as e:
		email.send("REDIS错误", '%s' % str(e))


def process_feedback(request):
    try:
        model = Feedback()
        model.ip = request.META['REMOTE_ADDR']
        model.ttime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
        model.url = request.POST.get('url','')
        model.content = request.POST.get('feedbackinfo','')
        model.email = request.POST.get('email','')
        model.save()
        return True
    except Exception as e:
        email.send("处理反馈错误", '%s' % str(e))
        return False


def obtain_hits(model_type):
    """随机获取6个视频作为推荐的视频

    Args:
        model_type 模型类型前缀
    Returns:
        recommendations 随机获取的视频对象信息列表
    """
    try:
        count = SWITCH[model_type].objects.all().count()
        rand_ids = random.sample(range(int(count*0.95), count), 6)
        recommendations = SWITCH[model_type].objects.filter(id__in=rand_ids)
        return recommendations
    except Exception as e:
        email.send("获取推荐信息时失败", '%s' % str(e))
        return []
