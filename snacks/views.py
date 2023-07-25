from django.shortcuts import render
from django.views.generic import  ListView, DetailView , CreateView , DeleteView , UpdateView
from .models import Snack
from django.urls import reverse_lazy


class SnackListView (ListView):
    template_name = 'snack_list.html'
    model = Snack

class SnackDetailView (DetailView):
    template_name = 'Snack_Detail.html'
    model = Snack

class SnackCreateView (CreateView):
    template_name = 'snack_create.html'
    model = Snack
    fields = ['name','purchaser','description']

class SnackUpdateView (UpdateView):
    template_name = 'snack_update.html'
    model = Snack
    fields="__all__"
    success_url=reverse_lazy('snacks')

class SnackDeleteView(DeleteView):
    template_name = 'snack_delete.html'
    model = Snack
    success_url=reverse_lazy('snacks')