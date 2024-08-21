from django.shortcuts import render, redirect
from .models import NatalChartAnalysis, zodaic


# Create your views here.
def horoscopes(request):
    return render(request,'user/horoscopes.html')

def daily(request):
    return render(request,'user/daily.html')
def weekly(request):
    return render(request,'user/weekly.html')
def monthly(request):
    return render(request,'user/monthly.html')
def yearly(request):
    return render(request,'user/yearly.html')

def service(request):
    return render(request,'user/service.html')

def chartanalysis(request):
    return render(request,'user/chartanalysis.html')

def reading(request):
    return render(request,'user/reading.html')




