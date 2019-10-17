from video import views
from django.urls import path
from django.conf.urls import url


urlpatterns = [
    path('', views.index),
    path('info/movie/<int:movie_id>/', views.display_movie_info),
    path('info/tvseries/<int:tvseries_id>/', views.display_tvseries_info),
    path('info/variety/<int:variety_id>/', views.display_variety_info),
    path('info/anime/<int:anime_id>/', views.display_anime_info),
    path('play/movie/<int:movie_id>/', views.play_movie),
    path('play/tvseries/<int:tvseries_id>/<int:episode>/', views.play_tvseries),
    path('play/variety/<int:variety_id>/<int:episode>/', views.play_variety),
    path('play/anime/<int:anime_id>/<int:episode>/', views.play_anime),
    path('player/', views.player),
    url(r'^classify/type/(\d+)/time/(\d+)/area/(\d+)/page/(\d+)/$', views.classify),
    url(r'^search/keyword/(.+)/page/(\d+)/$', views.search),
    url(r'^searchm/$', views.searchm),
    path('ranking/', views.ranking),
    path('redisdump/', views.redisdump),
    path('begfilm/', views.begfilm),
    path('feedback/', views.feedback),
    path('download/', views.download),
]
