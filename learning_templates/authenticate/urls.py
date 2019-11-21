
from django.urls import path , include
from . import  views

urlpatterns = [
    path('', views.home, name="home"),
    #path('new_home/', views.new_home, name="new_home"),
    path('new_home/', views.new_home, name="new_home"),
    path('login/', views.login_user, name="login"),
    path('logout/', views.logout_user, name="logout"),
    path('register/', views.register_user, name="register"),
    path('edit_profile/', views.edit_profile, name="edit_profile"),
    path('change_password/', views.change_password, name="change_password"),
]

