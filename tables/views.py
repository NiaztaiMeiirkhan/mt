from django.shortcuts import render
from django.http import JsonResponse
from .models import Table

def table_list(request):
    tables = list(Table.objects.values())
    return JsonResponse(tables, safe=False)

def available_tables(request):
    available = list(Table.objects.filter(is_available=True).values())
    return JsonResponse(available, safe=False)
