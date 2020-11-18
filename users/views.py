"""Users views."""
# 
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required
from django.db import IntegrityError

# Models
from django.contrib.auth.models import User
from users.models import Profile


def login_view(request):
    """Login view."""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        
        user = authenticate(request, username=username, password=password)
        if user:
            login(request, user)
            return redirect('feed')
        else:
            return render(request, 'users/login.html', {'error': 'invalid username and password'})

    return render(request, 'users/login.html')


def signup(request):
    """Sign up view"""
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        pwd_confirmation = request.POST['passwd_confirmation']

        if password != pwd_confirmation:
            return render(request, 'users/signup.html', {'error': 'password confirmation does not match'})
        try:
            user = User.objects.create_user(username=username, password=password)
        except IntegrityError as ie:
            return render(request, 'users/signup.html', {'error': 'Username is already in use'})

        user.first_name = request.POST['first_name']
        user.first_name = request.POST['last_name']
        user.first_name = request.POST['email']
        user.save()

        profile = Profile(user=user)
        profile.save

        return redirect('login')

    return render(request, 'users/signup.html')


@login_required
def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect('login')

