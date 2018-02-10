from django.db import models
from django.shortcuts import render
from django.http import HttpRequest,HttpResponse
from .models import Whisky
# Create your views here.
def Search(request, query):
    result = Whisky.objects.filter(name__icontains=query)
    return HttpResponse(result)