from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('note/', views.notes, name='notes'),
]
