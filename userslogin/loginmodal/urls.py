from django.urls import path
from . import views


urlpatterns = [
    path('', views.index, name='index'),
    path('portal/', views.portal, name='portal'),
    path('login/', views.Login, name='login'),
    path('userLogin', views.userLogin, name='userlogin'),
    path('userLogut/', views.userLogout, name='userlogout'),
]

