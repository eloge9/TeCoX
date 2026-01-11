from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import PetitionForm
from .models import Petition
# Create your views here.




def petition_view(request):

    # Si  le formulaire est soumis (method = POST)
    if request.method == 'POST':
        form = PetitionForm(request.POST) # On crée une instance du formulaire avec les données envoyées 
        if form.is_valid(): #Je vérifie si les données sont valides (par ex, si l'email est bien un mail)
            form.save() # Si c'est valide, on enregistre directement  dans la base de données 
            messages.success(request, 'Merci pour votre signature ! Votre soutien est précieux. ! ')
            return redirect('petition:petition') # Redirige vers la même page pour éviter la double soumission

    else: 
        form = PetitionForm() # 


    signature_count = Petition.objects.count()

    context = {
        'form': form,
        'signature_count': signature_count
    }
    
    return render(request, 'petition/petition.html', context)
