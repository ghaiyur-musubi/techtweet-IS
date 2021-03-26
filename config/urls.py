from django.contrib import admin
from django.urls import path
from tweets.views import feed , TweetDelete
from users.views import frontpage, signout, profile
from users.views import following, followers, follow, stopfollow


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('feed/', feed, name='feed'),
    path('signout/', signout, name='signout'),
    path('TweetDelete/<int:tweet_id>/', TweetDelete),
    path('<str:username>/', profile, name='profile'),
    path('<str:username>/following', following, name='following'),
    path('<str:username>/followers', followers, name='followers'),
    path('<str:username>/follow', follow, name='follow'),
    path('<str:username>/stopfollow', stopfollow, name='stopfollow'),
]