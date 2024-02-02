from django.urls import path
from .views import readpost

urlpatterns = [
    path('home/', readpost, name='readpost'),
]