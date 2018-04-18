# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse

from .models import Todo
# Create your views here.
def index(request):
  todos = Todo.objects.all()[:10]
  context = {
    'todos': todos
  }
  # return HttpResponse('Hello World')
  return render(request, 'index.html', context);

def details(request, id):
  todo = Todo.objects.get(id=id)
  context = {
    'todo': todo
  }
  # return HttpResponse('Hello World')
  return render(request, 'details.html', context);