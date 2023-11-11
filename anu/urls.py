from anu.views import *

from django.urls import path

app_name='something'

urlpatterns=[
    path('anu/',anu,name='anu.html')
]