from django.urls import path
from django.views.generic import TemplateView

from . import views

app_name="blog"

urlpatterns = [
    path('', views.my_form,name="homepage"),
    path('welcome/', views.welcome,name="welcome"),
    path('my_form/', views.my_form,name="form"),
]
