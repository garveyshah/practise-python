from django.urls import path
from . import views

urlpatterns = [
    path('', views.myworld, name='myworld'),
    path('members/', views.members, name='members'),
]