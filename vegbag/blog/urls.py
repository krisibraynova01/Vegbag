from django.urls import path, include

from vegbag.blog.views import blog, blog_details

urlpatterns = [
    path('', blog, name='blog'),
    path('details/<int:pk>/', blog_details, name='blog_details'),

]
