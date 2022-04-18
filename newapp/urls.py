from django.urls import path
from .views import index_page, handler404, vido_template

# from django.conf.urls import handler404

urlpatterns = [
    path('', index_page, name='index'),
    path('video/', vido_template, name='video')
]
