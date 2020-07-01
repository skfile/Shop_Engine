from django.shortcuts import render
from django.http import HttpResponse
# from django.db.models import Q
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


def search(request, q):
    template = 'searchstore/Search.html'

    if q:
        results = crawledData.objects.filter(Product_Name__icontains=q)
    else:
        results = crawledData.objects.all()
    context = {'products': results, 'input': q}

    return render(request, template, context)

    # query = request.GET.get(q)
    # if q:
    #     if query:
    #         results = crawledData.objects.filter(
    #             Product_Name__icontains=q)
    #     else:
    #         results = crawledData.objects.all()
    # else:
    #     results = crawledData.objects.all()


def searchEmpty(request):

    template = 'searchstore/Search.html'
    results = crawledData.objects.all()
    context = {'products': results, 'input': "-"}

    return render(request, template, context)
