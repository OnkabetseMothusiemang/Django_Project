from django.views.generic import ListView
from django.shortcuts import render
from .models import *

class HomeView(ListView):
    template_name ="tracking/home"
    context_object_name ="mydata"
    model = Locations
    success_url = "/"

# Create your views here.
