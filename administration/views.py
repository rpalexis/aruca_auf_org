from django.shortcuts import render

# Create your views here.
def adm_home(request):
    return render(request,'home_administration.html',{})
