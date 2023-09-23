from django.contrib.auth import views
from django.urls import path
from . import views

app_name = 'accounts'

urlpatterns = [
    path('registration/', views.registration, name='registration'),
    path('login/', views.login_view, name='login_view'),
    path('logout/', views.logout_view, name='logout_view'),
]
