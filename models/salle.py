"""
Module pour les salles
"""
from models.base_model import BaseModel

class Salle(BaseModel):
    """
    L'objet Salle
    """
    count = 0
    def __init__(self, name, cons):
        super().__init__(name, cons)
        Salle.count += 1