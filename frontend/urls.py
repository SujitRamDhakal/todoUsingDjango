from django.urls import path
from .views import *

urlpatterns = [
    path('viewlist/',list,name="viewlist"),
]
