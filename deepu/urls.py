from deepu.views import *

from django.urls import path

app_name='anything'

urlpatterns=[
    path('deepu/',deepu,name='deepu'),
]