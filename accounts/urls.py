from django.urls import path 
from .views import signup , user_activte , profile

app_name = 'accounts'


urlpatterns = [
    path('signup' , signup , name='signup'),
    path('profile' , profile , name='profile'),
    path('<str:username>/activate' , user_activte , name='user_activate')
]
