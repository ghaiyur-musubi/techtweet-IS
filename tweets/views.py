from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Tweet
from django.http import HttpRequest, HttpResponse, HttpResponseRedirect, HttpResponseBadRequest, JsonResponse
from .forms import TweetForm
from django.shortcuts import get_object_or_404
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User




@login_required
def feed(request):
    userids = []
    # Selects the user profile
    all_users = get_user_model()
    for user in all_users.objects.all():
        # collecting the IDs of user's following
        print('Found User ',user)
        userids.append(user.id)
        print("These are all the user ID Found",userids)
    tweets = Tweet.objects.filter(user_id__in=userids)

    return render(request, 'feed.html', {'tweets': tweets})


@login_required
def TweetDelete(request, tweet_id):
    # Get tweet
    tweet_to_delete = Tweet.objects.get(id=tweet_id)
    
    # Delete
    tweet_to_delete.delete()

    return HttpResponseRedirect('/'+request.user.username+'/')

# @login_required
# def like(request, username):
#     user = User.objects.get(username=username)
#     request.user.users.follows.add(user.users)

#     return redirect('/' + user.username + '/')


# @login_required
# def unlike(request, username):
#     user = User.objects.get(username=username)
#     # watch out, this should be .remove() instead of .delete()
#     request.user.users.follows.remove(user.users)

#     return redirect('/' + user.username + '/')

@login_required
def tweetLikeAdd(request, tweet_id):
  # Get requested tweet
  tweet = Tweet.objects.get(id = tweet_id)

  # Add count
  new_like_count = tweet.like_count + 1
  tweet.like_count = new_like_count

  # Save
  tweet.save()

  return JsonResponse({'result': 'successful'})

@login_required
def tweetLikeSubtract(request, tweet_id):
  # Get requested tweet
  tweet = Tweet.objects.get(id = tweet_id)

  # Subtract count
  new_like_count = tweet.like_count - 1
  tweet.like_count = new_like_count

  # Save
  tweet.save()

  return JsonResponse({'result': 'successful'})