from .models import Product

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializer import ProductSerializer


@api_view(["GET", "POST"])
def get_post_products(request):
    if request.method == "POST":
        data = request.data
        
        # fixing client side errors by using default values
        image = data.copy()
        for k, v in image.items():
            if v == "":
               del data[k]

        serializer = ProductSerializer(data=data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    if request.method == "GET":
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data)
    

@api_view(["GET", "PATCH", "DELETE"])
def get_patch_delete_product(request, pk):
    try:
        product = Product.objects.get(pk = pk)
    except:
        return Response(status=status.HTTP_404_NOT_FOUND)
    
    if request.method == "GET":
        serializer = ProductSerializer(product)
        return Response(serializer.data)
    
    if request.method == "PATCH":
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == "DELETE":
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)