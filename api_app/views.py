from django.http.response import HttpResponse
from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt
from django.contrib.auth.decorators import login_required

import json 
from api_app.models import IrisModel
from api_app.forms import IrisForm


# Create your views here.
@csrf_exempt
@login_required
def index(request):
    if request.method == "POST":
        form = IrisForm(request.POST)
        if form.is_valid():
            data = request.POST
            data = {
                'sepal_length' : data['sepal_length'],
                'sepal_width' : data['sepal_width'],
                'petal_length' : data['petal_length'],
                'petal_width' : data['petal_length'],
                'iris_class' : data['iris_class'],
            }
            instance = IrisModel.objects.create(**data)
            instance.save()


    response = "Service is up"
    return render(request,'index.html',context={'response':"Service is up",'form':IrisForm},content_type='text/html')
@csrf_exempt
@login_required
def viewDb(request):
    data = IrisModel.objects.all()
    return render(request,"db.html",{"data":data})
