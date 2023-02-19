from django.shortcuts import get_object_or_404, render
from django.urls import reverse_lazy
from django.views import generic
from django.views.generic.edit import CreateView, UpdateView, DeleteView

from .models import Bank, Supplier, BankAccount

#views bank
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

class SupplierListView(generic.ListView):
    model = Supplier



def supplier_detail(request, pk):
    supplier = get_object_or_404(Supplier, pk=pk)
    bank_accounts = BankAccount.objects.filter(nit__nit = supplier.nit).all()
    return render(request, 'bank/supplier_detail.html', {'supplier': supplier,'bank_accounts': bank_accounts})

class SupplierCreateView(CreateView):
    model = Supplier
    fields = ['name','nit','contact_person_name','contact_person_phone']

class SupplierUpdateView(UpdateView):
    model = Supplier
    fields = ['name','nit','contact_person_name','contact_person_phone']

class SupplierDeleteView(DeleteView):
    model = Supplier
    success_url = reverse_lazy('banks')
