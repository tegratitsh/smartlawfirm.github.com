from django.urls import path
from .import views




urlpatterns = [
    path('', views.smart_home_view, name='smart-home'),
]
