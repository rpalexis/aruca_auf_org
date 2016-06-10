from django.shortcuts import render
from django.http import HttpResponse
from annuaire.models import *
from ciec_portail.models import *
import csv
# Create your views here.
def adm_home(request):
    return render(request,'home_administration.html',{})

def instances(request):
    cdts = InstanceCandidature.objects.all()
    return render(request,'liste_instence.html',{'l_cndts':cdts})

def candidats(request):
    cdts = CandidatMembre.objects.all()
    return render(request,'liste_candidats.html',{'l_cndts':cdts})

def csv_exporting(request):
    # td = vari
    cdts = InstanceCandidature.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachement;filename="liste_instances.csv"'
    writer = csv.writer(response)
    writer.writerow(['Nom','Prenom','Sexe'])
    for moi in cdts:
        writer.writerow([moi.nom,moi.prenom,moi.sexe])
    return response

def csv_exporting_2(request):
    # td = vari
    cdts = CandidatMembre.objects.all()
    response = HttpResponse(content_type='text/csv')
    response['Content-Disposition'] = 'attachement;filename="listes_membres.csv"'
    writer = csv.writer(response)
    writer.writerow(['Nom','Prenom','Sexe'])
    for moi in cdts:
        writer.writerow([moi.nom,moi.prenom,moi.sexe])
    return response
