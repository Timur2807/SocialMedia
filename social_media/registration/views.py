
from django.contrib.auth import logout, login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.contrib import messages
from django.shortcuts import render, redirect

from .forms import SignUpForm
from .models import Profile


def registration(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        email = request.POST.get('email')
        if User.objects.filter(email=email).exists():
            form.add_error('email', 'Пользователь с таким email уже существует')
        phone_number = request.POST.get('phone_number')
        if User.objects.filter(phone_number=phone_number).exists():
            form.add_error(
                'phone_number',
                'Пользователь с таким номером телефона уже существует'
            )
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        if form.is_valid():
            user = form.save()
            # сохранение номера
            Profile.objects.create(user=user, phone_number=form.cleaned_data.get('phone_number'))
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            user.email = email
            user.first_name = first_name
            user.last_name = last_name
            user = form.save()
            form.save_m2m()
            login(request, user)
            messages.success(request, message='Вы успешно зарегистрировались')
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


