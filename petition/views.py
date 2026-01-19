from django.shortcuts import render, redirect
from .forms import PetitionForm
from .models import Petition
import base64
from django.core.files.base import ContentFile

def liste_petitions(request):

    petitions = Petition.objects.all().order_by('-created_at')
    return render(request, 'petition/liste_petitions.html', {'petitions': petitions})

def petition_view(request):
    if request.method == "POST":
        form = PetitionForm(request.POST)

        if form.is_valid():
            petition = form.save(commit=False)
            signature_base64 = request.POST.get("signature_base64")

            if signature_base64:
                format, imgstr = signature_base64.split(";base64,")
                ext = format.split("/")[-1]
                file = ContentFile(base64.b64decode(imgstr), name=f"signature.{ext}")
                petition.signature = file

            if not petition.niveau_soutien:
                petition.niveau_soutien = None

            petition.save()
            return redirect("petition:petition")

    else:
        form = PetitionForm()

    signature_count = Petition.objects.count()

    context = {
        'form': form,
        'signature_count': signature_count,
    }

    return render(request, "petition/petition.html", context)

