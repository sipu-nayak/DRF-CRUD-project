from django.db import models
import  datetime
class CompanyDetails(models.Model):
    id=models.IntegerField(primary_key=True)
    company_name=models.CharField(max_length=5)
    email_id=models.EmailField(max_length=20)
    company_code=models.CharField(max_length=5)
    created_time=models.TimeField()
