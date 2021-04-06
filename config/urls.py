from django.contrib import admin
from django.urls import path
from tweets.views import feed , TweetDelete
from users.views import frontpage, signout, profile
from users.views import following, followers, follow, stopfollow , tweetLikeAdd, tweetLikeSubtract


urlpatterns = [
    ### Pages
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('feed/', feed, name='feed'),
    path('signout/', signout, name='signout'),
    ### Tweet Activities
    path('TweetDelete/<int:tweet_id>/', TweetDelete),
    path('tweetLikeAdd/<int:tweet_id>/', tweetLikeAdd),
    path('tweetLikeSubtract/<int:tweet_id>/', tweetLikeSubtract),
    ### User Activities
    path('<str:username>/', profile, name='profile'),
    path('<str:username>/following', following, name='following'),
    path('<str:username>/followers', followers, name='followers'),
    path('<str:username>/follow', follow, name='follow'),
    path('<str:username>/stopfollow', stopfollow, name='stopfollow'),
]