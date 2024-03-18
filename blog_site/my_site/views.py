from django.http import HttpResponse
from django.shortcuts import render

def home(request):
    return render(request, 'index.html')

def main(request):
    return HttpResponse("Hey! It's your main view!!")

def test(request):
    return render(request, 'test.html')

def contacts(request):
    return render(request, 'contacts.html')
