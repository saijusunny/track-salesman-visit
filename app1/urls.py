from django.urls import path
from . import views
from django.contrib import admin

from django.contrib.auth.views import LogoutView

urlpatterns = [
    
    path('login/', views.CustomLoginView.as_view(), name='login'),
    path('logout/', LogoutView.as_view(next_page='login'), name='logout'),
    path('signup/', views.SignupPage.as_view(), name='signup'),
    path('', views.dashboard, name='dashboard'),
    

]

