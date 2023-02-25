
from django.shortcuts import render, redirect
from .models import Truck

def offer_truck(request):
    if request.method == 'POST':
        owner = request.POST.get('owner')
        capacity = request.POST.get('capacity')
        truck = Truck(owner=owner, capacity=capacity)
        truck.save()
        return redirect('list_trucks')
    return render(request, 'offer_truck.html')

def list_trucks(request):
    trucks = Truck.objects.all()
    return render(request, 'list_trucks.html', {'trucks': trucks})

def book_truck(request, truck_id):
    truck = Truck.objects.get(id=truck_id)
    if truck.is_available():
        truck.book(request.user.username)
        return redirect('list_trucks')
    return render(request, 'book_truck_failed.html')