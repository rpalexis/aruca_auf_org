# -*- encoding: utf-8 -*-
import re
from annuaire.models import Chercheur
from annuaire.utils import get_django_user_for_email
from django.conf import settings
from django.contrib.auth.backends import ModelBackend
from hashlib import md5


class PersonneBackend(ModelBackend):

    def authenticate(self, username=None, password=None):
        try:
            personne = Chercheur.objects.get(courriel=username, actif=True)
        except Chercheur.DoesNotExist:
            return None
        user = get_django_user_for_email(username)
        if settings.AUTH_PASSWORD_REQUIRED or user.check_password(password):
            return user
