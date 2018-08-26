from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('session/', views.createsession, name='createsession'),
    path('<session>/', views.go, name='go'),
]
