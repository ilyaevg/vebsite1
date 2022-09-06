from django.shortcuts import render
from django.http import HttpResponse


def index(reqeust):
    return HttpResponse('<h4>Hallo</h4>')


def detail(reqeust):
    return render(reqeust, 'detail.html')
