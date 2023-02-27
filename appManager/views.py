from django.shortcuts import render,redirect, resolve_url,reverse, get_object_or_404
from django.urls import reverse_lazy
from django.contrib.auth import get_user_model
from django.views.generic import CreateView,ListView,View,DetailView,UpdateView
from django.contrib.auth.views import LoginView
from .forms import RegistrationForm,LoginForm
from django.contrib.auth.mixins import LoginRequiredMixin
from .models import Profile
from django.contrib.auth import logout
from rest_framework import generics
from .serializers import ProfileSerializer
from django_filters import rest_framework as filters
from django_filters.rest_framework import DjangoFilterBackend
import django_filters
from django_filters import FilterSet, AllValuesFilter
from django_filters import  NumberFilter
  
class ProfileFilter(django_filters.FilterSet):
    min_age = django_filters.NumberFilter(field_name='age', lookup_expr='gte')
    max_age = django_filters.NumberFilter(field_name='age', lookup_expr='lte')

    class Meta:
        model = Profile
        fields = ['hometown', 'gender']
        

class ProfileList(generics.ListAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = ProfileFilter
    
    def get(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        serializer = self.get_serializer(queryset, many=True)
        print(serializer)
        context = {
            'profiles': serializer.data
            }
      
        return render(request,'dashboard/index.html',context)

class ProfileDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Profile.objects.all()
    serializer_class = ProfileSerializer
    lookup_field='username'
    lookup_url_kwarg='username'
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance)
        context = {
            'profile': serializer.data,
        }
        return render(request, 'dashboard/single.html', context)
    
    
class Register (CreateView):
    model = get_user_model()
    form_class  = RegistrationForm
    template_name = 'registrations/register.html'
    success_url = reverse_lazy('appManager:login')

    
class Login_View(LoginView):
    model = get_user_model()
    form_class = LoginForm
    template_name = 'registrations/login.html'
    def get_success_url(self):
        url = resolve_url('appManager:api')
        return url
 
class Logout_View(View):
    def get(self,request):
        logout(self.request)
        return redirect ('appManager:login',permanent=True)
  
