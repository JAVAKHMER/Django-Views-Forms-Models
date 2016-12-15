from django.conf.urls import url
from db.views import CompanyView, EmployeeView, AddressView

urlpatterns = [
    url(r'^$', CompanyView.as_view(), name='company_view'),
    url(r'^employees/$', EmployeeView.as_view(), name='employee_view'),
    url(r'^address/$', AddressView.as_view(), name='address_view'),
]
