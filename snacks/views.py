from django.shortcuts import render
from django.views.generic import TemplateView ,ListView, DetailView
from .models import Snack

class HomeView(TemplateView):
    template_name = 'home.html'

class SnackListView (ListView):
    template_name = 'snack_list.html'
    model = Snack

class SnackDetailView (DetailView):
    template_name = 'Snack_Detail.html'
    model = Snack

    