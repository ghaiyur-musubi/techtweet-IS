from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Tweet


@login_required
def feed(request):
    userids = []
    # Selects the user profile
    for user in request.user.users.follows.all():
        # collecting the IDs of user's following
        userids.append(user.id)
    tweets = Tweet.objects.filter(user_id__in=userids[:25])

    return render(request, 'feed.html', {'tweets': tweets})


@login_required
def TweetDelete(request, tweet_id):
  # Get tweet
  tweet_to_delete = Tweet.objects.get(id=tweet_id)
  
  # Delete
  tweet_to_delete.delete()

  return render(request, 'feed.html', {'tweets': tweets})