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