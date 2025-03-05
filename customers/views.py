from django.shortcuts import render, get_object_or_404
from django.http import JsonResponse
from .models import Customer

def customer_list(request):
    customers = list(Customer.objects.values())
    return JsonResponse(customers, safe=False)

def customer_detail(request, id):
    customer = get_object_or_404(Customer, id=id)
    return JsonResponse({"id": customer.id, "name": customer.name, "phone": customer.phone})
