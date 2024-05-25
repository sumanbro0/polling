
from django.contrib import admin
from django.urls import path
from .views import index,poll_detail,submit_poll,signin,register,delete_poll,lout



urlpatterns = [
    path('',index,name='index'),
    path('poll_detail/<int:id>/',poll_detail,name='poll_detail'),
    path('polls/<int:poll_id>/submit/', submit_poll, name='submit_poll'),
    path('login/',signin,name='login'),
    path('signup/',register,name='signup'),
    path('logout/',lout,name='logout'),
    path('delete_poll/<int:id>/',delete_poll,name='delete_poll'),

]
