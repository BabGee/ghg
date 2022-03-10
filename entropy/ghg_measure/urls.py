import imp
from django.urls import path
from ghg_measure.views import *


urlpatterns = [
    path('', index, name='index'),

]