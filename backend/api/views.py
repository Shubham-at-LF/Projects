import json
from rest_framework.response import Response
from rest_framework.decorators import api_view
from django.forms.models import model_to_dict
from prod.serializers import ProductSerializers
from prod.models import Product

@api_view(["GET","POST"])
def api_home(request, *args, **kwargs) :
    data = {}
    serializer = ProductSerializers(data = request.data)
    if serializer.is_valid() :
        instance = serializer.save()
        print(instance)
        data = serializer.data
    return Response(data)