from django.apps import AppConfig
from watson import search as watson

class AnnuaireConfig(AppConfig):
    name = "annuaire"
    def ready(self):
        ActualitesAO = self.get_model("ActualitesAO")
        watson.register(ActualitesAO)
        print("Actu")
        LaboEquip = self.get_model("LaboEquip")
        watson.register(LaboEquip)
        print("lab")
