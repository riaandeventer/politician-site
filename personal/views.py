from django.shortcuts import render
from django.contrib.auth.decorators import login_required

# Create your views here.
def index(request):
    return render(request, "index.html")

def about(request):
    return render(request, "about.html")

def programs(request):
    return render(request, "programs.html")

def contact(request):
    return render(request, "contact.html")

@login_required
def vips(request):
    return render(request, "vip.html")



