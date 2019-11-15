
from django.conf.urls import url
from django.urls import path
from .views import *

from rest_framework.routers import DefaultRouter

# GC = get_or_create_data()
urlpatterns = [
    url(r'^', view = WeatherListAPIView.as_view(), name = None),
    url(r'erase/(?P<w_id>\d+)',view=erase_data, name=None),
    url(r'^erase$', view = erase_by_date, name=None),
    url(r'^weather$', view = Get_or_Post.as_view(), name = None),
    url(r'^weather/temperature$',view = get_with_temperature, name = None),
]