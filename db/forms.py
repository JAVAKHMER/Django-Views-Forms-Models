from django.forms.models import ModelForm
from db.models import Company, Employee, Address
class CompanyForm(ModelForm):
    class Meta:
        model = Company
        fields = '__all__'
        
class EmployeeForm(ModelForm):
    class Meta:
        model = Employee
        fields = '__all__'
        
class AddressForm(ModelForm):
    class Meta:
        model = Address
        fields = '__all__'