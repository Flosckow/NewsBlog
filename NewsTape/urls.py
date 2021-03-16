
from django.urls import path
from django.views.decorators.csrf import csrf_exempt

from .views import *

urlpatterns = [
    path('', GetAllNews.as_view(), name='get_all_news'),
    path('post/', csrf_exempt(post_news), name='news_create'),
    path('one_news/<int:id>/', GetOneNews.as_view(), name='get_one_news')
]