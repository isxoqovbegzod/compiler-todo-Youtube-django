from django.urls import path
from .views import *

urlpatterns = [
    path('todo/', todo_page, name='todo')
]






