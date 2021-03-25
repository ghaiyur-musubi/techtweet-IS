from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from users.forms import SignupForm, SigninForm
from tweets.forms import TweetForm


def frontpage(request):
    if request.user.is_authenticated:
        return redirect('/' + request.user.username + '/')
    else:
        if request.method == 'POST':
            if 'signupform' in request.POST:
                signupform = SignupForm(data=request.POST)
                signinform = SigninForm()

                if signupform.is_valid():
                    username = signupform.cleaned_data['username']
                    password = signupform.cleaned_data['password1']
                    signupform.save()
                    user = authenticate(username=username, password=password)
                    login(request, user)
                    return redirect('/')

            else:
                signinform = SigninForm(data=request.POST)
                signupform = SignupForm()

                if signinform.is_valid():
                    login(request, signinform.get_user())
                    return redirect('/')

        else:
            signupform = SignupForm()
            signinform = SigninForm()

    return render(request, 'frontpage.html', {'signupform': signupform,
                                              'signinform': signinform})


@login_required
def signout(request):
    logout(request)
    return redirect('/')


@login_required
def profile(request, username):
    if request.user.is_authenticated:
        user = User.objects.get(username=username)

        if request.method == 'POST':
            form = TweetForm(data=request.POST)

            if form.is_valid():
                tweet = form.save(commit=False)
                tweet.user = request.user
                tweet.save()

                redirecturl = request.POST.get('redirect', '/')

                return redirect(redirecturl)
        else:
            form = TweetForm()

        return render(request, 'profile.html', {'form': form, 'user': user})

    else:
        return redirect('/')


@login_required
def following(request, username):
    user = User.objects.get(username=username)
    # important to add .all() at the end!
    users = user.users.follows.select_related('user').all()

    return render(request, 'users.html', {'title': 'Following',
                                          'users': users})


@login_required
def followers(request, username):
    user = User.objects.get(username=username)
    # important to add .all() at the end!
    users = user.users.followed_by.select_related('user').all()

    return render(request, 'users.html', {'title': 'Followers',
                                          'users': users})


@login_required
def follow(request, username):
    user = User.objects.get(username=username)
    request.user.users.follows.add(user.users)

    return redirect('/' + user.username + '/')


@login_required
def stopfollow(request, username):
    user = User.objects.get(username=username)
    # watch out, this should be .remove() instead of .delete()
    request.user.users.follows.remove(user.users)

    return redirect('/' + user.username + '/')