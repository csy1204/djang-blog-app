from django.shortcuts import render, redirect

from django.contrib.auth.models import User
from django.contrib import auth

# Create your views here.
def signup(request):
    if request.method == "POST":
        if request.POST['password1'] != request.POST['password2']:
            return render(request, template_name="signup.html")
        user = User.objects.create_user(request.POST['username'], password=request.POST['password1'])
        auth.login(request, user)
        return redirect('blog')
    return render(request, template_name="signup.html")

def login(request):
    if request.method == "POST":
        user = auth.authenticate(request, username=request.POST['username'], password=request.POST['password'])
        if user:
            auth.login(request, user)
            return redirect('blog')
        return render(request, "login.html", { 'error': 'There is no user'})
    return render(request, "login.html")

def logout(request):
    auth.logout(request)
    return redirect('blog')