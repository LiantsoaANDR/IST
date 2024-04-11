"""Module servant comme une sorte de base de donnees. Sauvegarde en fichier json"""
import json
from models.base_model import BaseModel
from models.appareil import Appareil
from models.salle import Salle


class FileStorage:
    """
    Classe servant pour le stockage et le chargement de nos donnees
    """
    __file_path = "sauvegarde.json"
    __objects = {}

    def all(self):
        """Retourne le dictionnaire de tous les objects"""
        return FileStorage.__objects
    
    def new(self, obj):
        """Met dans __objects l'objet avec comme cle : <nom de la classe de l'objet>.id"""
        key =  obj.__class__.__name__ + "." + obj.id
        FileStorage.__objects[key] = obj

    def save(self):
        """
        Sauvegarde tous les objets en fichier JSON
        """
        obj_dict= {}
        for key, value in FileStorage.__objects.items():
            obj_dict[key] = value.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """
        Transforme le fichier JSON en __objects (Seulement si ce fichier existe)
        """
        classes = {'BaseModel': BaseModel, 'Appareil': Appareil, 'Salle': Salle}
        try:
            with open(FileStorage.__file_path, "r") as f:
                object_dict = json.load(f)
                for key, val in object_dict.items():
                    self.all()[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass