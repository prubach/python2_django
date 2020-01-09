from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('t', views.test, name='test'),
    path('<int:cust_id>/', views.cust, name='customer')
]