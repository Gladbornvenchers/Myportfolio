from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Contact

# Create your views here.
def portfolio_home(request):

    return render(request, "portfolio/index.html")



def contact_page(request):
    if request.method == "POST":
        name = request.POST.get("name")
        email = request.POST.get("email")
        message = request.POST.get("message")

        Contact.objects.create(name=name, email=email, message=message)
        return HttpResponse(f"Message received from {name}!")
    return render(request, "portfolio/contact.html")