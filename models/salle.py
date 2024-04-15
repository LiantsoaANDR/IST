"""
Module pour les salles
"""
from models.base_model import BaseModel

class Salle(BaseModel):
    """
    L'objet Salle
    """
    count = 0
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        Salle.count += 1

    name = "SANS NOM"
    cons = 0