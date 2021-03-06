"""Users views."""
# 
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import redirect, render
from django.contrib.auth.decorators import login_required

# Forms
from users.forms import ProfileForm, SignupForm
from django.contrib import messages


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
        form = SignupForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = SignupForm()

    return render(request, template_name='users/signup.html', context={'form': form})


@login_required
def logout_view(request):
    """Logout a user."""
    logout(request)
    return redirect('login')


@login_required
def update_profile(request):
    """Update a user profile view"""
    profile = request.user.profile

    if request.method == 'POST':
        form = ProfileForm(request.POST, request.FILES)
        if form.is_valid():
            data = form.cleaned_data

            profile.picture = data['picture']
            profile.website = data['website']
            profile.biography = data['biography']
            profile.phone_number = data['phone_number']
            profile.save()
            messages.success(request, 'Your Profile has been update!')

            return redirect('update_profile')
    else:
        form = ProfileForm()

    return render(
        request= request, 
        template_name='users/update_profile.html',
        context={
            'profile': profile,
            'user': request.user,
            'form': form
            }
        )