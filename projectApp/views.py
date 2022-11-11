from .serializer import ProductMainSerializer
from .models import ProductMain
from rest_framework.decorators import api_view
from django.http import JsonResponse


# Create your views here.

@api_view(http_method_names=["GET"])
def get_all_products(request):
    products = ProductMain.objects.all()
    products_serialized = ProductMainSerializer(products, many=True)
    return JsonResponse(products_serialized.data, safe=False)
 
@api_view(http_method_names=["GET"])
def product(request,unique_code):   
    prod = ProductMain.objects.get(id=unique_code)
    serialized = ProductMainSerializer(prod)
    return JsonResponse(serialized.data, safe=False)