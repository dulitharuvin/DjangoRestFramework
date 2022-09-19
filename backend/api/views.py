import json
from django.forms.models import model_to_dict
from django.http import JsonResponse

from products.models import Product

def api_home(request, *args, **kwarg):
    model_data = Product.objects.all().order_by("?").first()
    data = {}
    if model_data:
        data['id'] = model_data.id
        data['title'] = model_data.title
        data['content'] = model_data.content
        data['price'] = model_data.price
        # model instance (model_data)
        # turn a python dict
        # return JSON to my client
    return JsonResponse(data)