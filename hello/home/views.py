from django.shortcuts import render
from home.models import Contact
from django.http import HttpResponse
from django.contrib import messages

def index(request):
    context = {
        "variable1": "911",
        "variable2": "034",
    }
    return render(request, 'index.html', context)

def about(request):
    return render(request, 'about.html')

def services(request):
    return render(request, 'services.html')

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
