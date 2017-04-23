from django.conf.urls import url
from django.contrib import admin

from concerts import views


urlpatterns = [
    url(r'^$', views.HomePageView.as_view(), name='home'),
    url(r'^bands/$', views.BandListView.as_view(), name='band_list'),
    url(r'^bands/band(?P<pk>\d+)/$', views.BandDetailView.as_view(),
        name='band_detail'),
    url(r'^cities/$', views.CityListView.as_view(), name='city_list'),
    url(r'^citys/city(?P<pk>\d+)/$', views.CityDetailView.as_view(),
        name='city_detail'),
    url(r'^concert(?P<pk>\d+)/$', views.ConcertDetailView.as_view(),
        name='concert_detail'),
    url(r'^stats/$', views.StatisticsView.as_view(), name='stats'),
    url(r'^admin/', admin.site.urls),
]
