import cmd
from models.base_model import BaseModel
from models.appareil import Appareil
from models.salle import Salle
from models import storage

class Shell(cmd.Cmd):

    class_list = ["BaseModel", "Appareil", "Salle"]

    prompt = '(estimateur) '

    def do_print(self, arg):
        print(arg)

    def do_quit(self, arg):
        return True

    def emptyline(self):
        """Ne fait rien"""
        pass

    def do_create(self, arg):
        """
        Crée un objet de son choix
        """
        arg_list = arg.split()
        if arg == "":
            print("** Veuillez entrer la classe de l'objet suivie de son nom puis de sa consommation **")
        elif arg_list[0] not in self.class_list:
            print("** Cette classe n'existe pas. Les classes sont: BaseModel, Appareil, Salle **")
        elif len(arg_list) == 1:
            print("** Entrer un nom du model **")
        elif len(arg_list) == 2:
            arg_list.append(0)
            obj = eval(arg_list[0])(arg_list[1], int(arg_list[2]))
            print(obj)
            obj.save()
        elif len(arg_list) > 3:
            print("** Trop d'argument. Les arguments doivent etre: Class Nom Consommation **")
        else:
            obj = eval(arg_list[0])(arg_list[1], int(arg_list[2]))
            print(obj)
            obj.save()

    def do_show(self, arg):
        """
        Print la representation de l'objet basée sur le nom de la classe et son identifiant unique
        """
        arg_list = arg.split()
        if arg == "":
            print("** Manque du nom de la classe **")
        elif arg_list[0] not in self.class_list:
            print("** Cette classe n'existe pas **")
        elif len(arg_list) < 2:
            print("** Manque de l'identifiant unique **")
        else:
            obj_key = arg_list[0] + "." + arg_list[1]
            if obj_key in storage.all():
                print(storage.all()[obj_key])
                return
            print("** L'objet n'existe pas **")

    def do_destroy(self, arg):
        """
        Supprime un object selon son nom de classe et son identifiant unique
        (sauvegarde les changements effectués)
        """
        arg_list = arg.split()
        if arg == "":
            print("** Manque du nom de la classe **")
        elif arg_list[0] not in self.class_list:
            print("** Cette classe n'existe pas **")
        elif len(arg_list) < 2:
            print("** Manque de l'identifiant unique **")
        else:
            obj_key = arg_list[0] + "." + arg_list[1]
            if obj_key in storage.all():
                storage.all().pop(obj_key)
                storage.save()
                return
            print("** L'objet n'existe pas **")

    def do_all(self, arg):
        """
        Prints toues les representations de tous les objects selon ou non leur nom de classe
        """
        obj_rep = []
        if arg == "":
            for obj in storage.all().values():
                obj_rep.append(str(obj))
            print(obj_rep)
        elif arg in self.class_list:
            for obj in storage.all().values():
                if obj.__class__.__name__ == arg:
                    obj_rep.append(str(obj))
            print(obj_rep)
        else:
            print("** L'objet n'existe pas **")

    def do_update(self, arg):
        """
        Met à jour l'objet selon son nom de classeet et de son identifiant en ajoutant ou mettant à jour son attribute
        (Enregistre les changements effectués)
        """
        arg_list = arg.split()
        if arg == "":
            print("** Manque du nom de la classe **")
        elif arg_list[0] not in self.class_list:
            print("** Cette classe n'existe pas **")
        elif len(arg_list) < 2:
            print("** Manque de l'identifiant unique **")
        elif len(arg_list) < 3:
            print("** Manque du nom de l'attribut **")
        elif len(arg_list) < 4:
            print("** Manque de la valeur de l'attribut **")
        else:
            obj_key = arg_list[0] + "." + arg_list[1]
            if obj_key in storage.all():
                setattr(
                        storage.all()[obj_key],
                        arg_list[2],
                        arg_list[3][1:-1]
                        )
                storage.save()
            else:
                print("** L'objet n'existe pas **")


if __name__ == '__main__':
    Shell().cmdloop()