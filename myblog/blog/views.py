# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.http import HttpResponse
from django.shortcuts import render

from . import models

# Create your views here.

def index(request):
    article = models.Artical.objects.get(pk=1);
    return render(request, 'blog/index.html',{'article' :article})



