from django.urls import path
from . import views

urlpatterns = [
    path('newpage',views.home, name='home'), #app02/newpage
    path('htmlpage',views.htmlpage, name='htmlpage'), #app02/htmlpage
    #path('add',views.add, name='add'),
    # path('newpage',views.newpage, name='newpage'),
    # path('page02',views.page02, name='newpage02'),
    
]