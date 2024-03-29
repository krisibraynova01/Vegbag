from django.urls import path

from vegbag.home.views import index

urlpatterns = [
    path('', index, name= "index")
]