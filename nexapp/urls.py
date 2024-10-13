from django.urls import path
from nexapp import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('login/', views.user_login, name='login'),
    path('signup/', views.signup, name='signup'),
    path('search/', views.search_colleges, name='search_colleges')
]

