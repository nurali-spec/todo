from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
def homepage(request):
    return HttpResponse("secont step")
def test(request):
    return render(request,"test.html")
