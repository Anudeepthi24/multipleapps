from deepthi.views import *

from django.urls import path

app_name='something'

urlpatterns=[
    path('deepthi/',deepthi,name='deepthi')
]

