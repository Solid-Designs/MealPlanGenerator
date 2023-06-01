from django.urls import path
# You can't just import views. It has to be from the current directory
from . import views

urlpatterns = [
    # You must set the path, import the function to give the view, then name it
    path('', views.index, name='index')
]
