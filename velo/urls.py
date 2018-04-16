from django.conf.urls import url
from . import views

urlpatterns = [
	url(r'^$', views.listeplayers, name='listeplayers'), #url de la page d'acceuil
	url(r'^player/(?P<pk>[0-9]+)/$', views.detailsplayer, name='detailsplayer'),
	url(r'^player/nouveau/$', views.newplayer, name='newplayer'),

]