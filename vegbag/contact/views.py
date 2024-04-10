from django.shortcuts import render, redirect
from django.urls import reverse_lazy
from django.views.generic import FormView

from vegbag.contact.forms import ContactForm


# Create your views here.

class ContactView(FormView):
    template_name = 'contact/contact.html'
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)
