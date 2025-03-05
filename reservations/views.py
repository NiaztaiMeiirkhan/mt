from django.shortcuts import get_object_or_404
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
import json
from .models import Reservation
from customers.models import Customer
from tables.models import Table
from django.shortcuts import render
from .models import Reservation
@csrf_exempt
def create_reservation(request):
    if request.method == "POST":
        data = json.loads(request.body)
        customer = get_object_or_404(Customer, id=data["customer_id"])
        table = get_object_or_404(Table, id=data["table_id"])

        if Reservation.objects.filter(table=table, date=data["date"]).exists():
            return JsonResponse({"error": "Table already reserved on this date"}, status=400)
        
        if Reservation.objects.filter(customer=customer, date=data["date"]).exists():
            return JsonResponse({"error": "Customer already has a reservation on this date"}, status=400)

        reservation = Reservation.objects.create(
            customer=customer,
            table=table,
            date=data["date"],
            status="pending"
        )
        return JsonResponse({"message": "Reservation created", "id": reservation.id})

def reservation_list(request):
    reservations = Reservation.objects.all()
    return render(request, 'reservations/list.html', {'reservations': reservations})

def create_reservation(request):
    return render(request, 'reservations/create.html')