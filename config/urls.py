from django.contrib import admin
from django.urls import path
from tweets.views import feed , TweetDelete, TweetLikeAdd, TweetLikeSubtract,like
from users.views import frontpage, signout, profile
from users.views import following, followers, follow, stopfollow


urlpatterns = [
    ### Pages
    path('admin/', admin.site.urls),
    path('', frontpage, name='frontpage'),
    path('feed/', feed, name='feed'),
    path('signout/', signout, name='signout'),
    ### Tweet Activities
    path('TweetDelete/<int:tweet_id>/', TweetDelete),
    path('TweetLikeAdd/<int:tweet_id>/', TweetLikeAdd),
    path('TweetLikeSubtract/<int:tweet_id>/', TweetLikeSubtract),
    path('like/', like, name='tweet-like'),
    ### User Activities
    path('<str:username>/', profile, name='profile'),
    path('<str:username>/following', following, name='following'),
    path('<str:username>/followers', followers, name='followers'),
    path('<str:username>/follow', follow, name='follow'),
    path('<str:username>/stopfollow', stopfollow, name='stopfollow'),
]