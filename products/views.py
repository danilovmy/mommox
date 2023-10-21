from django.views.generic.list import ListView
from django.http import JsonResponse
from django.forms.models import model_to_dict
from .models import Product

# Create your views here.

class ProductsView(ListView):

    model = Product

    def render_to_response(self, context, **response_kwargs):
        return JsonResponse(
            [self.serialize_result(obj)for obj in context["object_list"]], safe=False
        )

    def serialize_result(self, obj):
        return model_to_dict(obj)
