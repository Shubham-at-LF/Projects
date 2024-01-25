from rest_framework import generics, mixins,permissions, authentication
from .models import Product
from .serializers import ProductSerializers


class ProductCreateAPIView(generics.CreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    def perform_create(self, serializer):
        title = serializer.validated_data.get('title')
        content = serializer.validated_data.get('content') or None
        if content is None:
            content = title
        serializer.save(content = content)


class ProductListAPIView(generics.ListAPIView):
    queryset = Product.objects.all()
    serializer_class=  ProductSerializers
    authentication_classes = [authentication.SessionAuthentication]
    permission_classes =[permissions.IsAuthenticated]

# class ProductDetailAPIView(generics.RetrieveAPIView):
#     queryset = Product.objects.all()
#     serializer_class=  ProductSerializers

class ProductUpdateAPIView(generics.UpdateAPIView):
    queryset = Product.objects.all()
    serializer_class=  ProductSerializers
    lookup_field = 'pk'
    def perform_update(self, serializer):
        instance = serializer.save()
        if not instance.content:
            instance.content  = instance
            
class ProductDeleteAPIView(generics.DestroyAPIView):
    queryset = Product.objects.all()
    serializer_class=  ProductSerializers
    lookup_field = 'pk'
    def perform_destroy(self, instance):
         super().perform_destroy(instance)


class ProductMixinView(
    mixins.ListModelMixin,
    mixins.RetrieveModelMixin,
    generics.GenericAPIView
    ):
    queryset = Product.objects.all()
    serializer_class = ProductSerializers
    lookup_field = 'pk'

    def get(self ,  request ,  *args, **kwargs):
        pk = kwargs['pk']
        if pk is not None:
            return self.retrieve(request, *args, **kwargs)
        return self.list(request, *args, **kwargs)