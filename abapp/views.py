from django.shortcuts import render  # , redirect


# Create your views here.
def home(request):
    return render(request, "home.html", {})


def address(request):
    return render(request, "address.html", {})
