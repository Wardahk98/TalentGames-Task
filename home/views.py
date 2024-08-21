from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib.auth import login, logout, authenticate
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.

def home(request):
    return render(request, "index.html")


def register(request):
    if request.method == "POST":
        name = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        print(f"{name} - {email} - {password}")
        if User.objects.filter(email="email"):
            messages.info(request, "Email already register")
            return redirect("/register/")
        else:
            user = User.objects.create(
                username=name,
                email=email,
            )
            user.set_password(password)
            user.save()
            return redirect("/login/")
    return render(request, "register.html")


def login_page(request):
    if request.method == "POST":
        name = request.POST.get("username")
        password = request.POST.get("password")
        if User.objects.filter(username=name):
            user_exist = authenticate(request, username=name, password=password)
            if user_exist is None:
                messages.info(request, "No such user registered.")
                return redirect("/login/")
            else:
                login(request, user_exist)
                return redirect("/")
    return render(request, "login.html")


@login_required(login_url="/login/")
def logout_page(request):
    logout(request)
    return redirect("/")
