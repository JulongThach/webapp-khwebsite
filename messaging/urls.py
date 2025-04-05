from django.urls import path
from .views import *

urlpatterns = [

    path("", home, name="home"),
    
    path("message/", send_message, name="message"),
    path("about/", about, name="about"),
    path("price/", price, name="price"),
    path("success/", success, name="success"),
]
