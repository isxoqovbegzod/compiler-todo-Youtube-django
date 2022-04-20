from django.urls import path
from .views import index_page, handler404, vido_template, some_view

# from django.conf.urls import handler404

urlpatterns = [
    path('', index_page, name='index'),
    path('video/', vido_template, name='video'),
    path('captchat/', some_view, name='captchat')
]
