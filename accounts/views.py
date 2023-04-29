from django.shortcuts import render, redirect
from .models import Profile, Address, ContactNumbers
from django.contrib.auth.decorators import login_required


@login_required
def profile(request):
    profile = Profile.objects.get(user=request.user)
    address = Address.objects.filter(user=request.user)
    conact_numbers = ContactNumbers.objects.filter(user=request.user)
    return render(
        request,
        "accounts/profile.html",
        {"profile": profile, "address": address, "conact_numbers": conact_numbers},
    )
