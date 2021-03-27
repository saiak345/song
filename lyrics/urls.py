from django.urls import path

from lyrics.views import home
urlpatterns = [
    path('',home),
]
