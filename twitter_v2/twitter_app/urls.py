from django.urls import path
from .views import *



urlpatterns = [
    path('user-create/', createUser, name='user-create'),
    path('login/', auth, name='login'),
    path('logout/', logout_page, name='logout'),
]