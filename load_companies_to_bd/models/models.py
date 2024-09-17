import json

from django.db import models



# Create your models here.

class Company(models.Model):
    id = models.IntegerField(primary_key=True, unique=True)
    data = models.JSONField()

    @staticmethod
    def sync_companies(but):
        companies = but.call_list_method("crm.company.list")
        companies = {item['ID']: item for item in companies}

        companies_obj = []
        for index, data in companies.items():
            data_json = json.dumps(data)
            companies_obj.append(Company(id=index, data=data_json))

        if len(companies_obj) > 0:
            Company.objects.bulk_create(companies_obj, update_conflicts=True, unique_fields=['id'], update_fields=['data'])