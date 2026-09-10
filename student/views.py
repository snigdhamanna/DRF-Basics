from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def student(requuest):
    return HttpResponse('<h2> hello</h2>')