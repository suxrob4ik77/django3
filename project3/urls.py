from django.urls import path,include
from project3.views import *

urlpatterns = [
    path('west4/', last4),
    path('west5/', last5),
    path('west6/', last5),


]