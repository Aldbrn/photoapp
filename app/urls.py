from django.urls import path
from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("users/<int:pk>/", views.users_detail, name="user_detail"),
]
