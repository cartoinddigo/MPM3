from django.conf.urls import url
from . import views
urlpatterns = [
	url(r'^$', views.home, name='home'), #url de la page d'acceuil
	url(r'^nouveau/$', views.nouveau_site, name='nouveau_site'),
	url(r'^detail/', views.lstdetail, name='lstdetail'),
	url(r'^liste/', views.sites_liste, name='sites_liste'),
	url(r'^details/(?P<pk>[0-9]+)/$', views.site_detail, name='site_detail'),
	url(r'^delete/(?P<pk>\d+)/$', views.delete_site, name="delete_site"),
	url(r'^catalogue/', views.catalogue_liste, name="catalogue_liste"),
	url(r'^newcat/$', views.nouveau_catalogue, name="nouveau_catalogue"),
	url(r'^detcat/(?P<pk>[0-9]+)/$', views.catalogue_detail, name="catalogue_detail"),
	url(r'^batchcat/', views.batch_catalogue, name="batch_catalogue"),
]