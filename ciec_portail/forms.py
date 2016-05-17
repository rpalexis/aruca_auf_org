from django import forms
from .models import *
from django.core.exceptions import ValidationError

class InstanceCandidatureForm(forms.ModelForm):
    def clean(self):
        if(self.cleaned_data.get('sexe')=='f'):
            raise ValidationError(
            'Tu nas pas de sexe'
            )

        return self.cleaned_data
    class Meta:
        model = InstanceCandidature
        exclude = ('show',)



class CandidatMembreForm(forms.ModelForm):
    def clean(self):
        return self.cleaned_data
    class Meta:
        model = CandidatMembre
        exclude = ('show',)
