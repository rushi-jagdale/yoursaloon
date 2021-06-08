from django.urls import path
from projectapp import views

urlpatterns = [
    path('index/',views.home, name='index'),
    
]
