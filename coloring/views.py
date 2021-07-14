from django.shortcuts import render

def index(request):
    return render(request, 'coloring/index.html')

def home(request):
    return render(request, 'coloring/homepage.html')

def mybook(request):
    return render(request, 'coloring/mybook.html')

def templates(request):
    return render(request, 'coloring/templates.html')