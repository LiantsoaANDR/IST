"""
Module servant de base pour toutes les classes de notre projet
"""
import models
import uuid


class BaseModel:
    """ommateurs d'eau
    """
    count = 0
    id = None

    def __init__(self, *arg, **kwargs):
        """
        self : l'objet en question
        arg : non utilisé
        kwarg : dictionnaire de valeur de nos attributs (comme nom et consommation)
        """        
        if kwargs and len(kwargs) > 0:
            for key, value in kwargs.items():
                    self.__dict__[key] = value
        else:
            self.id = str(uuid.uuid4())
            models.storage.new(self)
    
    def __str__(self):
        """
        Retourne la representation de comment BaseModel devrait etre print-er
        """
        return ("L'objet de type '{}' de nom '{}' d'identifiant: {} a pour consommation {}".format(self.__class__.__name__, self.name, self.id, self.cons))

    def save(self):
        """
        Sauvegarde l'objet
        """
        models.storage.save()

    def to_dict(self):
        """
        Retourne un dictionnaire contenant tous les clés/valeurs de __dict__ de l'objet
        """
        base_dict = self.__dict__.copy()
        base_dict["__class__"] = self.__class__.__name__
        return base_dict    