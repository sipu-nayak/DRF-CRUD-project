from django.contrib import admin
from .models import CompanyDetails
@admin.register(CompanyDetails)
class CompanyAdmin(admin.ModelAdmin):
    list_display=['id','company_name','email_id','company_code','created_time']

