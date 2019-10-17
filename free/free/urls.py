from django.urls import path
from django.urls import include
from django.contrib import admin
from django.conf.urls import handler404
from django.conf.urls import handler500
import video.views

urlpatterns = [
    path('', include('video.urls')),
    path('admin/', admin.site.urls),
]

handler404 = video.views.page_not_found
handler500 = video.views.page_not_found
