from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse
from .models import ToDo
def homepage(request):
    return render(request,"todoIndex.html")
def test(request):
    todo_list = ToDo.objects.all()
    return render(request,"test.html", {"todo_list": todo_list})
