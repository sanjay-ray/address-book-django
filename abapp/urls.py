from django.urls import path
from . import views

urlpatterns = [
    path("", views.home, name="home"),
    path("address/add/", views.add_address, name="address"),
    path("address/edit/<address_id>", views.edit_address, name="edit_address"),
    path("address/delete/<address_id>", views.delete_address, name="delete_address"),
]
