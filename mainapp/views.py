from django.http import HttpResponse
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response
from django.http import JsonResponse
import json


def index(request):
    return render(request, "index.html",)


def login(request):
    return render(request, "login.html")


def register(request):
    return render(request, "register.html")


def help(request):
    nodes = models.Area.objects.all()
    return render(request, 'help.html', {'nodes': nodes})


def helpresult(request):
    nodeid = request.GET.get('nodeid')
    try:
        helpcon = models.Area.objects.get(id=nodeid).community
    except:
        helpcon = ''

    return HttpResponse(helpcon)