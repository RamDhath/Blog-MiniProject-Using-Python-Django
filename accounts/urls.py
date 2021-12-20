from django.urls import path
from . import views

urlpatterns = [
    path('signin_signup/', views.signin_signup, name='signin_signup'),
    path('logout/', views.logout, name='logout')
]
