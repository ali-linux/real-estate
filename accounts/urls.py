from django.urls import path
from .import views

urlpatterns = [
    path('login/',views.login, name = 'login'),
    path('register/',views.register, name = 'register'),
    path('dashboard/', views.dashboard, name = 'dashboard'),
    path('logout/', views.logout, name = 'logout'),
    path('password/reset/', views.password_reset_func, name = 'password_reset'),
    path('password/reset/done/<slug:token>', views.password_reset_done, name = 'password_reset_done'),
]