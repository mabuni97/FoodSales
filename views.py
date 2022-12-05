from http.client import HTTPResponse
from django.shortcuts import render
import pandas as pd
import os
from django.core.files.storage import FileSystemStorage
from .models import FoodSales
from tablib import Dataset
from export.resource import FoodResource

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from export.serializers import FoodSerializer
  
# Create your views here.
 
def Import_Excel_pandas(request):
     
    if request.method == 'POST' and request.FILES['myfile']:      
        myfile = request.FILES['myfile']
        fs = FileSystemStorage()
        filename = fs.save(myfile.name, myfile)
        uploaded_file_url = fs.url(filename)              
        empexceldata = pd.read_excel(filename)
        dbframe = empexceldata     
        for dbframe in dbframe.itertuples():
            obj = FoodSales.objects.create(order_date=dbframe.OrderDate,region=dbframe.Region, city=dbframe.City,
                                            category=dbframe.Category, product=dbframe.Product, quantity=dbframe.Quantity, unit_price=dbframe.UnitPrice,
                                          )           
            obj.save()
        return render(request, 'import_excel_db.html', {
            'uploaded_file_url': uploaded_file_url
            })   
    return render(request, 'import_excel_db.html')


 
def Import_excel(request):
    if request.method == 'POST' :
        Food =FoodResource()
        dataset = Dataset()
        new_food = request.FILES['myfile']
        data_import = dataset.load(new_food.read())
        result = FoodResource.import_data(dataset,dry_run=True)
        if not result.has_errors():
            FoodResource.import_data(dataset,dry_run=False)        
    return render(request, 'template/import_excel_db.html',{})


class Foodlist(APIView):
    """
    List all Transformers, or create a new Transformer
    """
  
    def get(self, request, format=None):
        product = request.data.get('product')
        food = FoodSales.objects.filter(product= product)
        serializer = FoodSerializer(food, many=True)
        return Response({'status':'Success','results':serializer.data},status=status.HTTP_200_OK)
  
    def post(self, request, format=None):
        product = request.data.get('product')
        food = FoodSales.objects.filter(product= product)
        serializer = FoodSerializer(food[:5], many=True)
        return Response({'status':'Success','results':serializer.data},status=status.HTTP_200_OK)