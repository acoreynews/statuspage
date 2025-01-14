from django.contrib import admin
from .models import Incident

# Register your models here.

class IncidentAdmin(admin.ModelAdmin):
  list_display = ("title", "date", "status",)

admin.site.register(Incident, IncidentAdmin)

