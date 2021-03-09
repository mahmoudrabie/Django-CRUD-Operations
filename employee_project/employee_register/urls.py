from django.urls import path, include
from . import views

app_name = 'employee_register'

urlpatterns = [
    # get and post req. for insert operation
    path('', views.employee_form, name='employee_insert'),
    # get and post req. for insert operation
    path('insert/', views.employee_form, name='employee_insert'),
    # get and post req. for update operation
    path('<int:id>/', views.employee_form, name='employee_update'),
    path('delete/<int:id>/', views.employee_delete, name='employee_delete'),
    # get req. to retrieve and display all records
    path('list/', views.employee_list, name='employee_list')
]
