from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from . import models
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger


def index(request):
    return render(request, "index.html",)