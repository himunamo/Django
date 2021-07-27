
from django.urls import path
from .views import *

urlpatterns = [

    path('cart' , CartView.as_view()),
]
from . import views
from django.urls import path, include
app_name='cart'
urlpatterns=[
    path('',views.index,name='index'),
]