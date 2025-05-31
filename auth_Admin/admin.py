from django.contrib import admin
from .models import UserSubmission

# Register your models here.

@admin.site.register(UserSubmission)
class UserSubmissionAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'phone')
    search_fields = ('name', 'phone')

