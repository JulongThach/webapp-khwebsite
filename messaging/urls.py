from django.urls import path
from .views import *

urlpatterns = [

    path("", home, name="home"),
    path("message/", send_message, name="send_message"),
    path("success/", success, name="success"),
]
