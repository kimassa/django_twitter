from django.conf.urls import url, include
from django.contrib import admin
from tweets.views import TweetListView
from .views import home

urlpatterns = [
     url(r'^admin/', admin.site.urls), #admin/
     url(r'^$', TweetListView.as_view(), name='home'), #/
     url(r'^tweet/', include('tweets.urls', namespace='tweet')),

]
