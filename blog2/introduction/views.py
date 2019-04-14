from django.shortcuts import render

def intro(request):
    return render(request, 'introduction/intro.html', name="intro")  
# Create your views here.
