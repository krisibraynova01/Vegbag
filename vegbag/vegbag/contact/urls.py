from django.urls import path

from vegbag.contact.views import ContactView

urlpatterns = [
    path('',ContactView.as_view(),name='contact')
]