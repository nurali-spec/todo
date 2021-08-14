from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
def homepage(request):
    return render(request,"todoIndex.html")
def test(request):
    return render(request,"test.html")
