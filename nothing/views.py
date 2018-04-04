from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.

def foo(request):
    print("bar")
    return HttpResponse('foo')