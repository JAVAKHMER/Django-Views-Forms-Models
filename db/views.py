from django.shortcuts import render

from django.views.generic.base import View
from django.http import HttpResponse
from db.forms import CompanyForm, EmployeeForm, AddressForm
from django.shortcuts import render
from db.models import Company, Employee, Address
class CompanyView(View):
    template_company = "company.html"

    def get(self,request):
        lcompany_form = CompanyForm()
        dictionary = dict(company_form = lcompany_form, company = Company.objects.all())
        return render(request, self.template_company, dictionary)
    def post(self,request):
        lpost_data = request.POST.copy()
        lcompany_form = CompanyForm(lpost_data)
        if lcompany_form.is_valid():
            lcompany_form.save()
        dictionary = dict(company_form = lcompany_form, company = Company.objects.all())
        return render(request, self.template_company, dictionary)
#     def hello(self, request):
#         text = """<h1>welcome to my app !</h1>"""
#         return HttpResponse(text)

class EmployeeView(View):
    def get(self,request):
        lemployees_form = EmployeeForm
        dictionaryEmployee = dict(employees_form = lemployees_form , employees = Employee.objects.all())
        return render(request, "employee.html",dictionaryEmployee)
    def post(self,request):
        lpost_data = request.POST.copy()
        lemployee_form = EmployeeForm(lpost_data)
        if lemployee_form.is_valid():
            lemployee_form.save()
            dictionaryEmployee = dict(employees_form = lemployee_form , employees = Employee.objects.all())
            return render(request, "employee.html",dictionaryEmployee)

class AddressView(View):
    def get(self,request):
        laddress_form = AddressForm
        dictionaryAddress = dict(address_form = laddress_form , address = Address.objects.all())
        return render(request,"address.html",dictionaryAddress)
    def post(self,request):
        lpost_data = request.POST.copy()
        laddress_form = AddressForm(lpost_data)
        if laddress_form.is_valid():
            laddress_form.save()
            dictionaryAddress = dict(address_form = laddress_form , address = Address.objects.all())
            return render(request,"address.html",dictionaryAddress)
