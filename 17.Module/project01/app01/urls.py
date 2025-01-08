from django.urls import path
from . import views

urlpatterns = [
    #path('',views.home, name='home'),
    path('newpage',views.newhome, name='newhome'),
    path('dynamic',views.dynamic, name='dynamic'),
    path('other',views.other, name='other'),
    path('',views.index, name='index'),

  
]