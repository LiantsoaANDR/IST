"""
Module pour les appareils
"""
from models.base_model import BaseModel

class Appareil(BaseModel):
    """
    L'objet appareil
    """
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    nom = "SANS NOM"
    user = 0
    cons = 0