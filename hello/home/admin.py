from django.contrib import admin
from home.models import Contact
from .models import IceCreamOrder
# Register your models here.
admin.site.register(Contact)
admin.site.register(IceCreamOrder)
