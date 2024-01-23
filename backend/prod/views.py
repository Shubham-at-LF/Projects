from rest_framework import generics
from .models import Product
from .serializers import ProductSerializers


class ProductCreateAPIView(generics.CreateAPIView):
    queryser = Product.objects.all()
    serializer_class = ProductSerializers
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content = content)



class ProductDetailAPIView(generics.RetrieveAPIView):
    queryset = Product.objects.all()
    serializer_class=  ProductSerializers