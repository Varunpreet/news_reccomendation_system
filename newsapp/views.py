from django.shortcuts import render
from .models import Data

# Create your views here.

def home(request):
    data = Data.objects.all()

    # context={'object2':obj2,'object3':obj3,'object4':obj4,'object5':obj5,'object6':obj6,'object7':obj7,'object8':obj8,'object9':obj9,'object10':obj10,'object11':obj11,'object12':obj12,'object13':obj13}

    return render(request, 'home.html', {'data': data})