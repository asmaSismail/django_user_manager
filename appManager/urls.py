from django.urls import path
from django.contrib import admin
from . import views
app_name = 'appManager'
urlpatterns = [
    path('admin/', admin.site.urls,name='admin'),
# Authentication Routes
    path('register/', views.Register.as_view(), name='reg'),
    path('', views.Login_View.as_view(), name='login'),
    path('logout/', views.Logout_View.as_view(), name='logout'),

    path('profileApi/', views.ProfileList.as_view(),name='api'),
    path('profileApi/<str:username>/', views.ProfileDetail.as_view(), name='Profile_detail'),
    ]
