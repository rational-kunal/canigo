from django.contrib.auth import login, authenticate, logout
from django.shortcuts import render, redirect

from .forms import SignUpForm, LoginForm


def sign_up(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
            return redirect('list_ticket')
    else:
        form = SignUpForm()
    return render(request, 'core/sign_up.html', {'form': form})


def sign_in(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password')
            user = authenticate(request, username=username, password=raw_password)
            if user:
                login(request, user)
                if user.is_staff:
                    return redirect('staff_home')
                else:
                    return redirect('user_home')
    else:
        form = LoginForm()
    return render(request, 'core/sign_in.html', {'form': form})


def sign_out(request):
    logout(request)

    return redirect('user_home')
