from django.urls import re_path as url
from . import views

urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^status/', views.status, name='status'),
]
