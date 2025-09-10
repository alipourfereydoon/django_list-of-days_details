from django.urls import path
from . import views

urlpatterns = [
    path('',views.list_days),
    path('<int:day>',views.dynamic_days_numbr),
    path('<str:day>',views.dynamic_days),
]
