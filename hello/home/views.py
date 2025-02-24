from django.shortcuts import render, redirect
from home.models import Contact
from django.http import HttpResponse
from django.contrib import messages
from django.http import JsonResponse
from .models import IceCreamOrder
from django.views.decorators.csrf import csrf_exempt
import json

def index(request):
    context = {
        "variable1": "911",
        "variable2": "034",
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')

        # Save the contact data to the database
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save()
 
        # return HttpResponse("Thank you for contacting us!")
        messages.success(request, "Your message has been sent.")
    return render(request, 'contact.html')

def order(request):
    return render(request, 'order.html')

# View to handle the form submission
@csrf_exempt  # Use this temporarily for testing; in production, handle CSRF properly
def save_order(request):
    if request.method == "POST":
        try:
            # Parse JSON data from the request body
            data = json.loads(request.body)
            icecream_name = data.get('icecream_name')
            quantity = data.get('quantity')

            # Save to the database
            order = IceCreamOrder(icecream_name=icecream_name, quantity=quantity)
            order.save()

            return JsonResponse({'status': 'success', 'message': 'Order saved successfully!'})
        except Exception as e:
            return JsonResponse({'status': 'error', 'message': str(e)}, status=400)
    return JsonResponse({'status': 'error', 'message': 'Invalid request method'}, status=405)