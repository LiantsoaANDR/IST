"""
Module pour les salles
"""
from models.base_model import BaseModel

class Salle(BaseModel):
    """
    L'objet Salle
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    nom = "SANS NOM"
    user = 0
    cons = 0