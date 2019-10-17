import abc
from base64 import b64encode
from video.models import Movie
from video.models import Tvseries
from video.models import Variety
from video.models import Anime
from video.models import Carousel
from video.config import SWITCH
from video.config import SWITCHU
from video.config import crypt
from video.features import obtain_hits
from video.ranking import index_ranking
from urllib.parse import unquote
from video.config import email


class ContextBase(metaclass=abc.ABCMeta):
    __context = {}  # 模板上下文对象

    @abc.abstractclassmethod
    def process(self):
        """封装模板上下文对象"""
        pass

    def context(self):
        """返回模板上下文对象"""
        return self.__context

    def _process_url(self, url):
        cipher_text = crypt.encrypt(url)
        self.__context['url'] = cipher_text

    def _process_history(self):
        """函数根据COOKIE中的信息将历史
        记录封装进模板上下文对象中"""
        paths = []  # 历史记录路径列表
        names = []  # 历史记录名称列表
        if 'whp' in self._request.COOKIES:
            paths = unquote(self._request.COOKIES['whp']).split('$$')
            paths.pop(0)
        if 'whn' in self._request.COOKIES:
            names = unquote(self._request.COOKIES['whn']).split('$$')
            names.pop(0)
        self.__context['paths'] = paths
        self.__context['names'] = names


class IndexContext(ContextBase):
    """封装首页中的视频信息上下文对象

    上下文对象中包含了首页中视频信息的对象列表，
    每个列表对应一个视频类型，包含十二个视频信息
    """
    def __init__(self, request):
        self._request = request

    def process(self):
        context = self.context()
        try:
            context['movie_items'] = Movie.objects.order_by('-id')[0:12]
            context['tvseries_items'] = Tvseries.objects.order_by('-id')[0:12]
            context['variety_items'] = Variety.objects.order_by('-id')[0:12]
            context['anime_items'] = Anime.objects.order_by('-id')[0:12]
            context['carousels'] = Carousel.objects.all()
            context['popular_videos'] = index_ranking()
            self._process_history()
            return True
        except Exception as e:
            return False


class MovieInfoContext(ContextBase):
    """封装电影信息的上下文对象

    上下文对象内的成员：
        info  电影信息 / actor 演员名字
        score 电影分数 / hits  热播视频
    """
    def __init__(self, request, movie_id):
        """
        Args:
            movie_id 电影ID
        """
        self._request = request
        self._movie_id = movie_id

    def process(self):
        context = self.context()
        try:
            info = Movie.objects.get(id=self._movie_id)
            context['info'] = info
            context['actor'] = info.actor
            context['score'] = info.score
            context['hits'] = obtain_hits('m')
            self._process_history()
            return True
        except Exception as e:
            return False


class VideoInfoContext(ContextBase):
    """封装电视剧/综艺节目/动漫信息的上下文对象

    类成员：
        _model 视频所属信息模型
        _u_model 视频所属播放模型
    上下文对象内的成员：
        info  视频信息 / actor 视频名字
        score 视频分数 / nums 视频的剧集数
        hits 热播的视频信息
    """

    def __init__(self, request, video_type, video_id):
        """
        Args:
            video_id 视频ID
            video_type 视频类型
                可能的值： 't'/'v'/'a'
        """
        self._request = request
        self._video_id = video_id
        self._video_type = video_type
        self._model = SWITCH[video_type]
        self._u_model = SWITCHU[video_type]

    def process(self):
        context = self.context()
        try:
            info = self._model.objects.get(id=self._video_id)
            nums = self._u_model.objects.values('url').filter(
                vid=self._video_id).count()  # 该视频的剧集总数
            context['info'] = info
            context['actor'] = info.actor
            context['score'] = info.score
            context['nums'] = range(0, nums)
            context['hits'] = obtain_hits(self._video_type)
            self._process_history()
            return True
        except Exception as e:
            return False


class PlayMovieContext(ContextBase):
    """该类封装电影播放信息的上下文对象
    上下文对象中仅包含电影的播放信息
    """

    def __init__(self, request, movie_id):
        """
        Args:
            movie_id 电影ID
        """
        self._request = request
        self._movie_id = movie_id

    def process(self):
        context = self.context()
        try:
            info = Movie.objects.get(id=self._movie_id)
            context['info'] = info
            self._process_url(info.url)
            self._process_history()
            return True
        except Exception as e:
            return False


class PlayVideoContext(ContextBase):
    """该类封装电视剧/综艺/动漫的播放信息上下文对象

    类成员：
        _model 视频所属信息模型
        _u_model 视频所属播放模型
    上下文对象内的成员：
        info 视频信息 / nums 当前视频剧集数
        url 当前视频的当前剧集的播放地址
    """

    def __init__(self, request, video_type, video_id, episode):
        """
        Args:
            video_id 视频ID
            video_type 视频类型 
                可能的值：'t'/'v'/'a'
            episode 当前剧集
        """
        self._request = request
        self._video_id = video_id
        self._video_type = video_type
        self._episode = episode
        self._model = SWITCH[video_type]
        self._u_model = SWITCHU[video_type]

    def process(self):
        context = self.context()
        try:
            info = self._model.objects.get(id=self._video_id)
            url = self._u_model.objects.get(
                vid=self._video_id, num=self._episode).url  # 当前剧集的播放地址
            nums = self._u_model.objects.values('url').filter(
                vid=self._video_id).count()  # 该视频的剧集总数

            context['info'] = info
            context['nums'] = range(0, nums)
            context['episode'] = self._episode
            
            self._process_url(url)
            self._process_pages(nums)
            self._process_history()
            return True
        except Exception as e:
            return False

    def _process_pages(self, nums):
        """完成对上下翻页信息的封装"""
        context = self.context()
        context['previous_episode'] = self._episode - 1
        context['next_episode'] = self._episode + 1
        if self._episode == 1:  # 不能再向前翻页
            context['previous_episode'] = 1
        if self._episode == nums:  # 不能再向后翻页
            context['next_episode'] = nums
