from django.shortcuts import render
from django.http import HttpResponse
from .forms import DataForm
from .models import *
from .forms import *


def home(request):
    context = {}
    return render(request, 'searchstore/Home.html', context)


def store(request):
    products = crawledData.objects.all()

    return render(request, 'searchstore/Store.html', {'products': products})


def contact(request):
    context = {}
    return render(request, 'searchstore/Contact.html', context)


def about(request):
    context = {}
    return render(request, 'searchstore/About.html', context)


def search(request, pk):

    form = DataForm()

    context = {}
    return render(request, 'searchstore/Search.html', context)
