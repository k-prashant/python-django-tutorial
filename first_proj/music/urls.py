from django.conf.urls import url, include
from . import views

app_name = 'music'

urlpatterns = [
	# /music/
    # url(r'^$', views.index, name='index'),
    url(r'^$', views.IndexView.as_view(), name='index'),

    # # /music/420
    # url(r'^(?P<album_id>[0-9]+)/$', views.detail, name='detail'),
    url(r'^(?P<pk>[0-9]+)/$', views.DetailView.as_view(), name='detail'),
    
    # # /music/420/favorite
    # url(r'^(?P<album_id>[0-9]+)/favorite$', views.favorite, name='favorite'),


    # # /music/album/add
    url(r'^album/add/$', views.AlbumCreate.as_view(), name='album-add'),
]
