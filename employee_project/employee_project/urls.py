from django.contrib import admin
from django.urls import path, include
from django.conf.urls.i18n import i18n_patterns

urlpatterns = [
    #path('', include('employee_register.urls', namespace='employee_register')),
    path('admin/', admin.site.urls),
    #path('employee/', include('employee_register.urls', namespace='employee_register')),
]

urlpatterns += i18n_patterns(
    path('', include('employee_register.urls', namespace='employee_register_i18n')),
)
