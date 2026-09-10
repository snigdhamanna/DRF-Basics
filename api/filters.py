import django_filters
from employee.models import *

class EmployeeFilter(django_filters.FilterSet):
    designation = django_filters.CharFilter(field_name='designation',lookup_expr='iexact')
    emp_id = django_filters.RangeFilter(field_name='emp_id')  # if want to give emp_id as EMP101 , RANGE filter will not work so we need advance filter

    
    class Meta:
        model = Employee
        fields = ['designation','emp_id']