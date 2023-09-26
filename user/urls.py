from django.contrib import admin
from django.urls import path 

from .views import ajouter_participant, participant_view

urlpatterns = [
    path('participant_view/', participant_view, name='participant_view'), 
    path('', ajouter_participant, name='ajouter_participant'), 
   # path('soumettre_deces/', soumettre_deces, name='soumettre_deces'), 

]