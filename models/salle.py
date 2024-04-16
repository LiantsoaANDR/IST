"""
Module pour les salles
"""
from models.base_model import BaseModel

class Salle(BaseModel):
    """
    L'objet Salle

    Attribut(s):
        nom : nom de la salle
        user : nomber d'utilisateur utilisant la salle
        cons : consommation en eau de la salle de chaque utilisateur
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    nom = "SANS NOM"
    user = 0
    cons = 0