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
        help_text='Придумайте уникальное имя пользователя.',
    )
    email = forms.EmailField(
        label='Почта Эл.',
        help_text='Введите электронную почту.',
    )

    class Meta:
        model = User
        fields = ('username', 'phone_number', 'email', 'password1', 'password2', )
