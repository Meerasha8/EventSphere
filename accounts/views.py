from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth import login,authenticate,logout
from django.contrib.auth import get_user_model
from django.contrib.auth.decorators import login_required
from .models import Profile

# Create your views here.

User = get_user_model()

def home_page(request):
    return render(request,"home.html")

def register(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email")
        role = request.POST.get("role")
        
        user = User.objects.create_user(
            username=username,
            password=password,
            email=email,
            role = role
        )
        Profile.objects.create(user=user)
        
        
        login(request,user)
        
        return redirect("/")
    
    return render(request,"auth/register.html")


def login_view(request):
    if request.method == "POST":
        username = request.POST.get("username")
        password = request.POST.get("password")
        
        user = authenticate(request,username=username,password=password)
        
        
        if user is not None:
            login(request,user)
            return redirect("/")
        return redirect("/login")
        
    return render(request,"auth/login.html")

def logout_view(request):
    logout(request)
    return redirect("/")


    

