from django.shortcuts import render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Bank

class BankListView(generic.ListView):
    model = Bank
    context_object_name = 'bank_list'

class BankDetailView(generic.DetailView):
    model = Bank
    context_object_name = 'bank'

class BankCreateView(CreateView):
    model = Bank
    fields = ['name']

class BankUpdateView(UpdateView):
    model = Bank
    fields = ['name']

class BankDeleteView(DeleteView):
    model = Bank
    success_url = reverse_lazy('banks')