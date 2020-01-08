from django.contrib import admin
from .models import Log

class LogAdmin(admin.ModelAdmin):
  list_display = ('title', 'dateAndTime')

# Register your models here.

admin.site.register(Log, LogAdmin)