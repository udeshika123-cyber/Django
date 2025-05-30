from django.urls import path
from . import views

urlpatterns = [
    path('myFirstApp/', views.myFirstApp, name='myFirstApp'),
]