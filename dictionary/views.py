from django.shortcuts import render

# Create your views here.
def index(request):
    return render(request,"dictionary/index.html")


def login(request):
    return render(request,"dictionary/login.html")