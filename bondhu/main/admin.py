from django.contrib import admin
from .models import History, Profiles

# Register your models here.
admin.site.register(Profiles)
admin.site.register(History)