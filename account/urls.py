from django.urls import path
from account import views

app_name = 'account'

urlpatterns = [
    path('login',views.loginview,name='login'),
    path('logout',views.logoutuser,name='logout'),
    path('register',views.usereg,name='register'),
]
