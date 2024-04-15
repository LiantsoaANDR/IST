"""
Module pour les appareils
"""
from models.base_model import BaseModel

class Appareil(BaseModel):
    """
    L'objet appareil
    """
    count = 0
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Appareil.count += 1

    name = "SANS NOM"
    cons = 0