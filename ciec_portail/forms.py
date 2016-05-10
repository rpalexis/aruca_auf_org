from django import forms
from .models import *

class InstanceCandidatureForm(forms.ModelForm):

    class Meta:
        model = InstanceCandidature
        exclude = ('show',)
