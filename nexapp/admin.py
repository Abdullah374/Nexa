from django.contrib import admin
from .models import College
from import_export.admin import ImportExportModelAdmin
# Register your models here.

@admin.register(College)
class data_college(ImportExportModelAdmin):
    pass
