import time
from video.models import Begfilm
from video.context import ContextBase
from video.config import BEGFILM_PROMPT

class BegFilm(ContextBase):
    def __init__(self, request):
        self._request = request
    
    def process(self):
        context = self.context()
        try:
            context['tips'] = BEGFILM_PROMPT
            self._process_history()
            return True
        except Exception as e:
            return False

    def process_begfilm(self):
        try:
            model = Begfilm()
            model.ip = self._request.META['REMOTE_ADDR']
            model.ttime = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime())
            model.content = self._request.POST.get('beginfo','')
            model.save()
            return True
        except Exception as e:
            return False
