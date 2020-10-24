from django.shortcuts import render
from . import models
from django.views.generic import TemplateView
# Create your views here.
def offer_view(request):
    offer_list = models.offer.objects.order_by('offer_id')
    offer_dict = {'offers':offer_list}
    return render(request, 'bananaApp/index.html', context=offer_dict)

def dyn_view(request, my_id):
    obj = models.offer.objects.get(id=my_id)
    context = {
        "object": obj
    }
    return render(request, 'bananaApp/offer.html', context)
