# diagnosis/admin.py
from django.contrib import admin
from .models import Diagnosis

class DiagnosisAdmin(admin.ModelAdmin):
    list_display = ('score_min', 'score_max', 'message')
    search_fields = ('message',)

# Register the model in the admin panel
admin.site.register(Diagnosis)
