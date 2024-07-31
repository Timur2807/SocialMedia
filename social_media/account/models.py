from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from django.db.models.signals import post_save
from django.dispatch import receiver


# class Profile(models.Model):
#     GENDER_CHOICE = [
#         ('M', 'M'),
#         ('F', 'Ж'),
#         (None, '-'),
#     ]
#
#     user = models.OneToOneField(User, on_delete=models.CASCADE)
#     avatar = models.ImageField(
#         'Аватар', blank=True,
#         upload_to='avatar/',
#         default='avatar/standard.jpg'
#     )
#     gender = models.CharField('Пол', max_length=1, choices=GENDER_CHOICE, blank=True)
#     city = models.CharField('Город', max_length=20, blank=True)
#     birth_date = models.DateField('Дата рождения', null=True, blank=True)
#
#     def __str__(self):
#         return str(self.user)
#
#     class Meta:
#         verbose_name = "Профиль"
#         verbose_name_plural = 'Профили'
#
# @receiver(post_save, sender=User)
# def create_user_profile(sender, instance, created, **kwargs):
#     if created:
#         Profile.objects.create(user=instance)
#
# @receiver(post_save, sender=User)
# def save_user_profile(sender, instance, **kwargs):
#     instance.profile.save()
