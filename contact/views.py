# -*- encoding: utf-8 -*-
from django.shortcuts import render_to_response
from django.template import Context, RequestContext
from django import forms
from django.core.mail import send_mail

class ContactForm(forms.Form):
    nom = forms.CharField(max_length=200)
    email = forms.EmailField(max_length=200, required=False)
    sujet = forms.CharField(max_length=200)
    message = forms.CharField(widget=forms.Textarea)

def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            message = request.POST.get('message', '')
            send_mail('Contact depuis le site ARICA', message ,'webmestre@auf.org',['marc.nachin@auf.org'])
            message = 'Votre mail a bien été transmis'                                                                                                                                        
    else:
        message = ''
        form = ContactForm() # An unbound form

    return render_to_response('contact.html', {'contact_form' : form, 'message' : message }, context_instance = RequestContext(request))
