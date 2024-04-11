"""
Module pour les appareils
"""
from models.base_model import BaseModel

class Appareil(BaseModel):
    """
    L'objet appareil
    """
    count = 0
    def __init__(self, name, cons):
        super().__init__(name, cons)
        Appareil.count += 1