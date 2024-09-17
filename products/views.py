#from django.shortcuts import render
from django.http import  JsonResponse, HttpResponse
from .models import Products
import json
from django.views.decorators.csrf import csrf_exempt
@csrf_exempt


# Create your views here.
def index(request, pk = None):
    #return HttpResponse("Hola, estoy  en la vista productos")

    if request.method == 'GET':
        if pk:
            product = Products.objects.get(id_product = pk)
            return JsonResponse(data={"message": "ok",
                                      "id": product.id_product,
                                      "name": product.name_prod,
                                      "price":product.price_prod,
                                      "stock":product.stock_prod})
        else:
            products = list(Products.objects.all().values("id_product",
                                                    "name_prod",
                                                    "price_prod",
                                                    "stock_prod"))
        #retun HttpRespose(productos)
        return JsonResponse(data={'message':'ok', 'Products':products})

    if request.method == 'POST':
        body = request.body.decode('utf-8')
        request_body = json.loads(body)
        
        product = Products.objects.create(
            
            id_product = request_body['id'],
            name_prod = request_body['name'],
            price_prod = request_body['price'],
            stock_prod = request_body['stock']
        )
        return JsonResponse(data={'message':'ok', 'id':product.id_product, 'name':product.name_prod, 'price':product.price_prod, 'stock':product.stock_prod})
    

    if request.method == 'DELETE':
        if pk:
            Products.objects.filter(id_product=pk).delete()
            return JsonResponse(data={"message": "product with id = " * str(pk) + " eliminado"})
        
    return HttpResponse('Metodo no disponible', status=406)
    
                                

