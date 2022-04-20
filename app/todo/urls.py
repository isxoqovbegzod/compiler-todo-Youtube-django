from django.urls import path
from .views import *

urlpatterns = [
    path('todo/', todo_page, name='todo'),
    path('todo/delete/<str:user>/<int:id>', delete, name='delete'),
    path('todo/update/<str:user>/<int:id>', update, name='update'),
]






