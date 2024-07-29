from django.urls import path
from .views import *

app_name = 'registration'


urlpatterns = [
    path('signup/', registration, name='registration'),
    path('welcome/', welcome, name='welcome'),
    path('logout/', logout_user, name='logout_user'),
    path('login/', login_user, name='login_user'),
]
