from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name='home'), 
    # path('add',views.add, name='add'),
    # path('newpage',views.newpage, name='newpage'),
    # path('page02',views.page02, name='newpage02'),
    
]