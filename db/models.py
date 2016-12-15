from __future__ import unicode_literals

from django.db import models
class Company(models.Model):
    company_name = models.CharField(max_length=50)
    companyPhone = models.CharField(max_length = 20)
    def __unicode__(self):
        return self.company_name
class Employee(models.Model):
    firstName = models.CharField(max_length = 50)
    lastName = models.CharField(max_length = 50)
    phone = models.CharField(max_length = 20)
    comapany = models.ForeignKey(Company)
    def __unicode__(self):
        return self.firstName
class Address(models.Model):
    street = models.CharField(max_length = 100)
    city = models.CharField(max_length = 100)
    employee = models.OneToOneField(Employee)