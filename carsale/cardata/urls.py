from cardata import views
from django.urls import path, include

urlpatterns=[
    path('',views.alldata,name='alldata')
]