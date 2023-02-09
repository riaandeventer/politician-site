from django.http import HttpResponseRedirect
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from .forms import NewUserForm

# Create your views here.
def login_user(request):
    return render(request, 'authorize/login.html')

def logout_user(request):
    logout(request)
    messages.info(request, "You have successfully logged out.") 
    return redirect("personal:home")

def register_user(request):
    if request.method == "POST":
        form = NewUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful." )
            return redirect("personal:home")
        messages.error(request, "Unsuccessful registration. Invalid information.")
    form = NewUserForm()
    return render (request=request, template_name="register/register.html", context={"register_form":form})

def authorize_user(request):
    username = request.POST['username']
    password = request.POST['password']
    user = authenticate(username=username, password=password)
    if user is None:
        messages.error(request, "Invalid username or password.")
        return HttpResponseRedirect(reverse('user_auth:login'))
    else:
        login(request, user)
        return HttpResponseRedirect(reverse('personal:home'))

