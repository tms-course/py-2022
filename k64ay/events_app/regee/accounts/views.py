from django.shortcuts import render, redirect
from django.contrib.auth import \
    logout, authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.urls import reverse

def logout_user(request):
    logout(request)

    return redirect(reverse('event_list'))


def register_user(request):
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
            
            return redirect('event_list')

    else:
        form = UserCreationForm()

    return render(request, 
                  'registration/register.html', 
                  {'form': form})