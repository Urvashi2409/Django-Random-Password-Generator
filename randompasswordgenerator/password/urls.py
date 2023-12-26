from django.urls import path
from . import views 

urlpatterns = [
    path("password/", views.generate_password),
]