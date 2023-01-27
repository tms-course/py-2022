from django.shortcuts import render, redirect
from .models import User
from .forms import RegistrationForm
from django.http import HttpResponseForbidden


def index(request):
    return render(request, 'index.html', {'list': User.objects.all()})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.save()
            return redirect('index')
    else:
        form = RegistrationForm
    return render(request, 'register.html', {'form': form})


def update_user(request, id: int):
    try:
        user = User.objects.get(pk=id)
    except:
        return HttpResponseForbidden()
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user_form = form.save(commit=False)
            user.first_name = user_form.first_name
            user.second_name = user_form.second_name
            user.phone_number = user_form.phone_number
            user.birth_date = user_form.birth_date
            user.save()
            return redirect('index')

    form = RegistrationForm
    return render(request, 'update.html', {'form': form})

