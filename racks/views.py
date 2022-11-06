from django.shortcuts import render

from django.http import HttpResponse
from django.http import Http404
from racks.models import rack_Azure

def index(request):
    items = rack_Azure.objects.all()
    return render(request, 'mystorage/index.html',{
        'items': items,
         })



def item_detail(request,id):
    try:
        item=rack_Azure.objects.get(id=id)
    except Item.DoesNotExit:
         raise Http404('This item does not exit')
    return render(request,'mystorage/item_detail.html',{
        'item':item,
 })
