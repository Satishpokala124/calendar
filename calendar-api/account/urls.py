from django.urls import path, include
from .views import user_login, register, user_logout

urlpatterns = [
    path('login/', user_login),
    path('register/', register),
    path('logout/', user_logout)
]