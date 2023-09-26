from django.shortcuts import render
from django.shortcuts import redirect, render
from django.shortcuts import render
from datetime import date

from user.models import Participant
# Create your views here.

def participant_view(request):
    participants = Participant.objects.all()
    return render(request, 'users/participant.html', {'participants': participants})

def ajouter_participant(request):
    if request.method == "POST":
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        number = request.POST.get('number')
        email = request.POST.get('email')

        
        naissance = Participant.objects.create(first_name=first_name, last_name=last_name,  number=number, email=email)
        print(naissance)
  
        print('Valideeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeeee')      
        return redirect('participant_view')

   
    else:
        print('non validesssssssssssssssssssssssssssssssssssssssssssssssssss')
        return render(request, 'users/inscrit_participant.html')