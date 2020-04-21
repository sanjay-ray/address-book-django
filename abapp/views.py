from django.shortcuts import render, redirect
from .models import Address
from .forms import AddressForm
from django.contrib import messages


# Create your views here.
def home(request):
    all_addresses = Address.objects.all
    return render(request, "home.html", {"all_addresses": all_addresses})


def add_address(request):
    if request.method == "POST":
        form = AddressForm(request.POST or None)
        if form.is_valid():
            form.save()
            messages.success(request, "New address has been successfully added.")
            return redirect("home")
        else:
            messages.success(request, "There was an error.")
            return render(request, "add_address.html", {})
    else:
        return render(request, "add_address.html", {})


def edit_address(request, address_id):
    if request.method == "POST":
        current_address = Address.objects.get(pk=address_id)
        form = AddressForm(request.POST or None, instance=current_address)
        if form.is_valid():
            form.save()
            messages.success(request, "The address has been successfully edited.")
            return redirect("home")
        else:
            messages.error(request, "There was an error.")
            return render(request, "edit_address.html", {})
    else:
        this_address = Address.objects.get(pk=address_id)
        return render(request, "edit_address.html", {"this_address": this_address})


def delete_address(request, address_id):
    if request.method == "POST":
        current_address = Address.objects.get(pk=address_id)
        current_address.delete()
        messages.success(request, "The address has been successfully deleted.")
        return redirect("home")
    else:
        messages.error(request, "There is nothing to delete.")
        return redirect("home")
