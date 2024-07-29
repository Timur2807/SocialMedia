
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.shortcuts import render, redirect

from .forms import SignUpForm
from .models import Profile


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            # сохранение номера
            Profile.objects.create(user=user, phone_number=form.cleaned_data.get('phone_number'))
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('registration:welcome')
    else:
        form = SignUpForm()
        context = {
            'form': form,
            'error': form.errors
        }
    return render(request, 'registration/signup.html', context)

def welcome(request):
    user = request.user
    context = {
        'user': user,
    }
    return render(request, 'registration/welcome.html', context)

def logout_user(request):
    if request.method == "POST":
        logout(request)
        return redirect('account:home')



def login_user(request):
    if request.method == 'GET':
        context = {
            'form': AuthenticationForm()
        }
        return render(request, 'registration/login.html', context)
    else:
        user = authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is None:
            context = {
                'form': AuthenticationForm(),
                'error': 'Неверные данные'
            }
            return render(request, 'registration/login.html', context)
        else:
            login(request, user)
            return redirect('registration:welcome')


