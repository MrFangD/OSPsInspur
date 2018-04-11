from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger
from django.shortcuts import render_to_response


def index(request):
    return render(request, "index.html",)


def login(request):
    nodes = models.Area.objects.all()
    return render(request, "login.html", {'nodes': nodes})


def register(request):
    return render(request, "register.html")


def help(request):
    nodes = models.Area.objects.all()
    return render(request, 'help.html', {'nodes': nodes})