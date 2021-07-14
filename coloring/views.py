from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def home(request):
    return render(request, 'coloring/homepage.html')