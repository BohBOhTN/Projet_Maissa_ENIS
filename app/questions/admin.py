# questions/admin.py
from django.contrib import admin
from .models import Question

class QuestionAdmin(admin.ModelAdmin):
    list_display = ('text', 'category', 'response_jamais', 'response_parfois', 'response_souvent', 'response_toujours')
    search_fields = ('text', 'category')

# Register the model in the admin panel
admin.site.register(Question)