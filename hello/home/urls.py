from django.contrib import admin
from django.urls import path
from home import views

urlpatterns = [
    path('', views.index, name='home'),
    # path('order', views.order, name='order'),
    path('about/', views.about, name='about'),
    path('contact', views.contact, name='contact'),
    path('order', views.order, name='order'),  # URL for the order page
    path('save_order/', views.save_order, name='save_order'),  # URL for saving the order
]