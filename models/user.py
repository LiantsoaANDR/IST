"""
Module pour les utilisateurs
"""
from models.base_model import BaseModel

class User(BaseModel):
    """
    L'objet Utilisateur
    """
    count = 0
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        User.count += 1

    age = 0