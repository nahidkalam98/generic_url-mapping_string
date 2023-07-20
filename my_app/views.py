from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def string_1(request):
    return HttpResponse('<h1 align="center">I am learning Python at JSpiders</h1>')

def string_2(request):
    return HttpResponse('<marquee><i><b>I am Nahid Kalam, a student of PYD-M1 Batch at Jspiders</b></i></marquee>')
