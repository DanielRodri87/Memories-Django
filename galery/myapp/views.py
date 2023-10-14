from django.shortcuts import render
from django.views.generic import TemplateView
from.models import *
from django.db.models import Sum
# importar Q
from django.db.models import Q

class HomeView(TemplateView):
    template_name = "home.html"
    