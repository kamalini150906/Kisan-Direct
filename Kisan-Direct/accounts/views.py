from django.contrib.auth import login
from django.shortcuts import render, redirect
from .forms import RegisterForm

def register(request):
    form = RegisterForm(request.POST or None)
    if form.is_valid():
        login(request, form.save())
        return redirect('home')
    return render(request, 'form.html', {'form': form, 'title': 'Create your account', 'button': 'Sign up'})
