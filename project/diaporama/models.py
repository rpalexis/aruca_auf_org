from django.db import models


class Slider(models.Model):
    image = models.ImageField(null=True, blank=True, upload_to='slider')
    titre = models.CharField(max_length=200)
    lien = models.CharField(max_length=200, null=True, blank=True)
    date_pub = models.DateTimeField('date de creation', auto_now=True)
    status = models.CharField(max_length=1, default='3', null=False, blank=False, choices=(('1', 'En cours de redaction'), ('2', 'Propose a la publication'), ('3', 'Publie en Ligne'), ('4', 'A supprimer')))