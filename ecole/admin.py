from django.contrib import admin
from .models import Inscription

# Register your models here.


class AdminInscription(admin.ModelAdmin):
    list_display = ['nom','email','numero']
    list_filter = ['nom']
admin.site.register(Inscription,AdminInscription)
