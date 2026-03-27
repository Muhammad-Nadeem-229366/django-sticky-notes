from django.contrib import admin
from .models import Note

# yahan hum Note model ko Django admin panel me register kar rahe hain
# is se hum admin panel se notes ko dekh, add, edit aur delete kar sakte hain
admin.site.register(Note)

# Register your models here.