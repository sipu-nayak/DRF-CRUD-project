from rest_framework import serializers
from .models import CompanyDetails
class CompanySerializer(serializers.ModelSerializer):
    class Meta:
        model=CompanyDetails
        fields=['id','company_name','email_id','company_code','created_time']
        