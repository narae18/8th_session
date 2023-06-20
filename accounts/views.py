from django.shortcuts import render, redirect
from django.contrib import auth
from django.contrib.auth.models import User
from users.models import Profile

# Create your views here.

def login(request):
    if request.method == 'POST':

        username = request.POST['username']
        password = request.POST['password']
        user = auth.authenticate(request, username=username, password=password)
    
        if user is not None:
            auth.login(request, user)
            return redirect('main:mainpage')

        else:
            return render(request, 'accounts/login.html')

    elif request.method == 'GET':
        return render(request, 'accounts/login.html')



def logout(request):
    auth.logout(request)
    return redirect('main:mainpage')



def signup(request):
    if request.method == 'POST':
        password = request.POST['password']
        confirm = request.POST['confirm']
        
        if password == confirm:
            username = request.POST['username']
            user = User.objects.create_user(username=username, password=password)

            nickname = request.POST['nickname']
            department = request.POST['department']
            reason = request.POST['reason']

            profile = Profile(user=user, nickname=nickname, department=department, reason=reason)
            profile.save()

            auth.login(request, user)
            return redirect('main:mainpage')
        else:
            return render(request, 'accounts/signup.html', {'error': 'Passwords do not match'})

    return render(request, 'accounts/signup.html')



    
