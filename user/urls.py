from django.urls import path

from . import views

app_name = 'user'
urlpatterns = [
    path('login', views.LoginView.as_view(), name="login"),
    path('join', views.JoinView.as_view(), name="join"),
]