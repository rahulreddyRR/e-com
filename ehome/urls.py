from django.urls import path
from ehome import views

app_name = 'ehome'

urlpatterns = [
    path('home',views.home,name='ehome')
]
