from django.contrib import admin
from django.urls import path
from contapp import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('',views.emp_view)
]
