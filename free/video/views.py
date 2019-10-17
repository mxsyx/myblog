from video.context import *
from django.http import HttpResponse
from django.http import JsonResponse
from django.shortcuts import render
from video.classify import ClassifyContext
from video.search import SearchContext
from video.ranking import RankingContext
from video.dump import RedisDump
from video.features import add_play_volume
from video.begfilm import BegFilm
from video.config import ERROR_MESSAGE
from video.config import crypt
from video.features import process_feedback


def index(request):
    contextobj = IndexContext(request)
    if contextobj.process():
        return render(request, 'index.tpl', contextobj.context())
    return HttpResponse(ERROR_MESSAGE)


""" 处理视频信息页面 """

def display_movie_info(request, movie_id):
    contextobj = MovieInfoContext(request, movie_id)
    if contextobj.process():
        return render(request, 'info/infomovie.tpl', contextobj.context())
    return HttpResponse(ERROR_MESSAGE)


def display_tvseries_info(request, tvseries_id):
    contextobj = VideoInfoContext(request, 't', tvseries_id)
    if contextobj.process():
        return render(request, 'info/infotvseries.tpl', contextobj.context())
    return HttpResponse(ERROR_MESSAGE)


def display_variety_info(request, variety_id):
    contextobj = VideoInfoContext(request, 'v', variety_id)
    if contextobj.process():
        return render(request, 'info/infovariety.tpl', contextobj.context())
    return HttpResponse(ERROR_MESSAGE)


def display_anime_info(request, anime_id):
    contextobj = VideoInfoContext(request, 'a', anime_id)
    if contextobj.process():
        return render(request, 'info/infoanime.tpl', contextobj.context())
    return HttpResponse(ERROR_MESSAGE)


""" 处理视频播放页面 """

def play_movie(request, movie_id):
    contextobj = PlayMovieContext(request, movie_id)
    if contextobj.process():
        add_play_volume('m', movie_id)
        return render(request, 'play/playmovie.tpl', contextobj.context())
    return HttpResponse(ERROR_MESSAGE)


def play_tvseries(request, tvseries_id, episode):
    contextobj = PlayVideoContext(request, 't', tvseries_id, episode)
    if contextobj.process():
        add_play_volume('t', tvseries_id)
        return render(request, 'play/playtvseries.tpl', contextobj.context())
    return HttpResponse(ERROR_MESSAGE)


def play_variety(request, variety_id, episode):
    contextobj = PlayVideoContext(request, 'v', variety_id, episode)
    if contextobj.process():
        add_play_volume('v', variety_id)
        return render(request, 'play/playvariety.tpl', contextobj.context())
    return HttpResponse(ERROR_MESSAGE)


def play_anime(request, anime_id, episode):
    contextobj = PlayVideoContext(request, 'a', anime_id, episode)
    if contextobj.process():
        add_play_volume('a', anime_id)
        return render(request, 'play/playanime.tpl', contextobj.context())
    return HttpResponse(ERROR_MESSAGE)


def player(request):
    try:
        cipher = request.POST.get('cipher','')
        plain_text = crypt.decrypt(cipher)
        context = {'url': plain_text}
        return JsonResponse(context)
    except UnicodeDecodeError:
        return HttpResponse('Hello, my friend')
    except Exception as e:
        return HttpResponse(str(e))


def classify(request, video_type, video_time, video_area, page):
    """ 处理视频分类页面 """
    contextobj = ClassifyContext(request, int(video_type), int(video_time), int(video_area), int(page))
    if contextobj.process():
        return render(request, 'classify.tpl', contextobj.context())
    return HttpResponse(ERROR_MESSAGE)


def search(request, keyword, page):
    """ 处理视频搜索页面 """
    contextobj = SearchContext(request, keyword, int(page))
    if contextobj.process():
        return render(request, 'search.tpl', contextobj.context())
    return HttpResponse(ERROR_MESSAGE)


def searchm(request):
    """ 处理移动端视频搜索页面 """
    return render(request, 'searchm.tpl')
    

def ranking(request):
    """ 处理视频排行页面 """
    contextobj = RankingContext(request)
    if contextobj.process():
        return render(request, 'ranking.tpl', contextobj.context())
    return HttpResponse(ERROR_MESSAGE)


def redisdump(request):
    """ 处理REDIS持久化页面 """
    redisdump = RedisDump()
    tips = "DUMP成功"
    if not redisdump.dump():
        tips = "DUMP失败"
    return render(request, 'tips.tpl', {'tips': tips})


def begfilm(request):
    """ 处理求片留言页面 """
    contextobj = BegFilm(request)
    if request.method == 'GET':
        if contextobj.process():
            return render(request, 'begfilm.tpl', contextobj.context())
        else:
            return HttpResponse(ERROR_MESSAGE)
    else:
        response = HttpResponse()
        if contextobj.process_begfilm():
            response.status_code = 200
        else:
            response.status_code = 500
        return response


def feedback(request):
    """ 处理求片反馈页面 """
    response = HttpResponse()
    if process_feedback(request):
        response.status_code = 200
    else:
        response.status_code = 500
    return response


def download(request):
    """ 处理下载页面 """
    return render(request, 'download.tpl')


def page_not_found(request):
    """ 404页面未找到 """
    return render(request, '404.tpl')
