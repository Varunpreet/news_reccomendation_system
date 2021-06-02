from django.shortcuts import render
from .models import Data

# Create your views here.

def home(request):
    data = Data.objects.all()

    return render(request,'home.html',{'data':data})