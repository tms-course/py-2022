from django.shortcuts import render, redirect, get_object_or_404
from .models import User
from .forms import RegistrationForm


def index(request):
    return render(request, 'index.html', {'list': User.objects.all()})


def register(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('index')
    else:
        form = RegistrationForm
    return render(request, 'register.html', {'form': form})


def update_user(request, id: int):
    user = get_object_or_404(User, pk=id)
    if request.method == 'POST':
        form = RegistrationForm(request.POST, instance=user)
        if form.is_valid():
            user = form.save()
            user.save()
            return redirect('index')

    form = RegistrationForm
    return render(request, 'update.html', {'form': form})

