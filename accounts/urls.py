from django.urls import path
from .views import profile, activate_account, signup, dashboard

app_name = "accounts"

urlpatterns = [
    path("profile", profile, name="profile"),
    path("signup/", signup, name="signup"),
    path("<str:username>/activate", activate_account, name="activate_account"),
    path("dashboard", dashboard, name="dashboard"),
]
