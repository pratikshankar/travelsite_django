from django.urls import path
from . import views

urlpatterns=[
    path('',views.home,name='home'),   # url path which is left blank ,views.home is the function, we give the name as "home"
    path('add',views.add,name='add'),
    path('muls',views.mul,name='mul')
    ]