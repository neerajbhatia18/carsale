from django.shortcuts import render
from .models import *

# Create your views here.
def alldata(request):

    customer=Customer.objects.all,
    records=Daily_Records.objects.all,
    vehicle=Vehicle.objects.all
    return render(request,'alldata.html',{'customers':customer,'records':records,'vehicles':vehicle})

