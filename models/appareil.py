"""
Module pour les appareils
"""
from models.base_model import BaseModel

class Appareil(BaseModel):
    """
    L'objet appareil

    Attribut(s):
        nom : nom de l'appareil
        user : nomber d'utilisateur utilisant l'appareil
        cons : consommation en eau de l'appareil de chaque utilisateur
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    nom = "SANS NOM"
    user = 0
    cons = 0