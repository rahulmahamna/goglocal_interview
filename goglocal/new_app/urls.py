from django.contrib import admin
from django.urls import include, path
from new_app.views import Login, Profile

urlpatterns = [
    path("user/login/", Login.as_view(), name="login"),
    path("user/profile/", Profile.as_view(), name="login"),
]