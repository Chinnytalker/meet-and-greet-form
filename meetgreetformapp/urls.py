from django.urls import path
from . import views





urlpatterns = [
    path("", views.fan_meet_and_greet, name="fan_meet_and_greet"),
    path("success/", views.success, name="success"),
    path("payment/", views.payment, name="payment"),
    path("payment_details/", views.payment_details, name="payment_details" ),
]