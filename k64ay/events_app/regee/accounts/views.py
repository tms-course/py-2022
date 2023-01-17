from django.shortcuts import render, redirect
from django.contrib.auth import logout
from django.urls import reverse

def logout_user(request):
    logout(request)

    return redirect(reverse('event_list'))
