from django.urls import path
from .views import *
from . import views
urlpatterns = [
    path('',views.home, name='home'),
    path('about/',views.about, name='about'),
    path('students/',views.students, name='students'),
    path('',views.home, name='home'),
]