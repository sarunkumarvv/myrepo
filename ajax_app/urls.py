from . import views
from django.urls import path


urlpatterns=[ 
      path('',views.home,name='home'),
      path('add_data/',views.add_data,name='add_data'),
]