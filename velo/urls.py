from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.home, name='home'), #url de la page d'acceuil
	url(r'^player/(?P<pk>[0-9]+)/$', views.detailsplayer, name='detailsplayer'),
	url(r'^player/nouveau/$', views.newplayer, name='newplayer'),
	url(r'^player/liste/$', views.listeplayers, name='listeplayers'),

]