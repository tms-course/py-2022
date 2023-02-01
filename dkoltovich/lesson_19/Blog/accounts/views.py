from django.shortcuts import render, reverse, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import \
    logout, authenticate, login


def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(
                username=username,
                password=raw_password)
            login(request, user)
            return redirect('feed')
    else:
        form = UserCreationForm()

    return render(request,
                  'registration/register.html',
                  {'form': form})


def logout_user(request):
    logout(request)
    return redirect(reverse('feed'))
