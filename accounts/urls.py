from django.urls import path
from .views import profile

app_name = "accounts"

urlpatterns = [
    path("profile", profile, name="profile"),
]
