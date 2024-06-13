from django.shortcuts import render
from django.contrib.auth import authenticate
from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import *
from .models import *

# Create your views here.

# class LoginView(APIView):
#     def post(self,request):
#         try:
#             serializer =LoginSerializer(data =request.data)
#             if serializer.is_valid():
#                 email =serializer.validate_data('email')        
#                 password=serializer.validate_data('password')   
                
#                 if not CustomUser.objects.filter(email=email).exists():
#                     return Response(self, responseData={
#                         'responseCode' :status.HTTP_404_NOT_FOUND,
#                         'responseData ': 'email not found',
                        
#                     })
                
#                 user =authenticate(email=email, password=password)
                
#                 if user is not None:
#                     refresh =RefreshToken.for_user(user)
#                     access =str(refresh.access_token)
#                     refresh =str(refresh)
#                     return  Response({
#                     'refresh': str(refresh),
#                     'access': str(refresh.access_token),
#                     })
                    
#                 return Response({'detail': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
                    
#         except Exception as e:
#             return  Response({'error ': e}, status=status.HTTP_401_UNAUTHORIZED)

from django.urls import reverse_lazy
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm
from django.views.generic.edit import FormView
from django.views.generic.list import ListView
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import CustomUser

class LoginView(FormView):
    template_name = 'auth/login.html'
    form_class = AuthenticationForm
    success_url = reverse_lazy('user_list')

    def form_valid(self, form):
        user = form.get_user()
        auth_login(self.request, user)
        return super().form_valid(form)
    
    
class UserListView(LoginRequiredMixin, ListView):
    model = CustomUser
    template_name = 'auth/user_list.html'
    context_object_name = 'users'

