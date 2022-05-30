from django.urls import path
from .views import html_template
urlpatterns = [
    path('', html_template, name='bosh')
]