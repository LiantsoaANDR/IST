"""
Module servant de base pour toutes les classes de notre projet
"""
import models
import uuid


class BaseModel:
    """
    Le modele de base de nos objets et salles consommateurs d'eau
    """
    count = 0

    def __init__(self, name=None, cons=0):
        """
        self : l'objet en question
        name : le nom de l'objet créé
        cons : la consommation en eau, en entier
        """
        if name is None:
            raise ValueError("** Veuillez inserer un nom svp **")

        if cons < 0:
            raise ValueError("** La consommation doit etre >= 0 **")
        
        self.name = name
        self.cons = cons
        BaseModel.count += 1
        # l'id est nécessaire car il est possible que plusieurs objets possèdent le même nom. d'où la nécessité d'un identifiant(id) unique
        self.id = str(uuid.uuid4())
        models.storage.new(self)
    
    def __str__(self):
        """
        Retourne la representation de comment BaseModel devrait etre print-er
        """
        return ("L'objet {} de numero {} a pour consommation {}".format(self.name, self.id, self.cons))

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