from django.db import models
from django.contrib.auth.models import User
from django import forms

class Profile(models.Model):
    email = forms.EmailField(
        label='Электронная почта',
        required=True,
        help_text='Пожалуйcта, введите ваш email.'
    )
    user = models.OneToOneField(User, on_delete=models.CASCADE,)
    phone_number = models.CharField(max_length=15)
    birth_date = models.DateField(null=True, blank=True)


    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Этот адрес электронной почты уже используется.')
        return email

