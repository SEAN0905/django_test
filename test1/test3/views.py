from django.shortcuts import render

def index(request):
    return render(request, "test3/index.html")

def sign(request):
    return render(request, "test3/sign.html")
