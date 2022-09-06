from django.shortcuts import render
from django.http import HttpResponse


def index(reqeust):
    return render(reqeust, 'index.html')


def about(reqeust):
    return render(reqeust, 'about.html')
