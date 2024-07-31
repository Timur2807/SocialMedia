from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class SignUpForm(UserCreationForm):
    phone_number = forms.CharField(
        label='Номер телефона',
        max_length=15,
        required=True,
        help_text='Номер телефона формата +7..',
    )
    username = forms.CharField(
        max_length=150,
        required=True,
        help_text='Придумайте уникальное имя пользователя.',
    )
    email = forms.EmailField(
        label='Почта Эл.',
        help_text='Введите электронную почту.',
        required=True,
    )

    first_name = forms.CharField(
        label='Имя',
        help_text='Введите Ваше имя',
        required=True,
    )

    last_name = forms.CharField(
        label='Фамилия',
        help_text='Введите Вашу фамилию',
        required=True,
    )

    error_messages = {
        'duplicate_username': 'Пользователь с таким именем уже существует',
        'password_mismatch': 'Пароли не совпадают'
    }

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'phone_number', 'email', 'password1', 'password2', )
