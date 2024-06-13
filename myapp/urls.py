from django.urls import path
from .views import *
from rest_framework.views import APIView

urlpatterns= [
    # path('login/', LoginView.as_view(), name ='login'),
    path('login/', LoginView.as_view(), name='login'),
    path('users/', UserListView.as_view(), name='user_list'),
    
    
]
