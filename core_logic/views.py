from django.urls import reverse_lazy
from django.views.generic import ListView, CreateView, UpdateView, DeleteView
from django.http import HttpResponse
from django.shortcuts import get_object_or_404, redirect
from .models import Expense as expense_model

# Create your views here.
class HomePageView(ListView):
    model = expense_model
    template_name = 'home.html'

class CreateEntryView(CreateView):
    model = expense_model
    template_name = 'form_expense.html'
    fields = ["name", "type", "price", "currency"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_name'] = "Create Form"
        return context

class UpdateEntryView(UpdateView):
    model = expense_model
    template_name = 'form_expense.html'
    fields = ["name", "price", "currency", "type"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['form_name'] = "Edit Form"
        return context

class DeleteEntryView(DeleteView):
    model = expense_model
    template_name = 'form_delete.html'
    success_url = reverse_lazy('home')


# Some utility functions
def redirect_main(request):
    return redirect('home')

def delete_entry(request, pk: int):
    if request.method == 'POST':
        try:
            expense_entry = get_object_or_404(expense_model, pk=pk)
            expense_entry.delete()
            return redirect('home')
        except Exception as e:
            return HttpResponse(status=400, content=f"Error deleting item: {e}") #type: ignore
