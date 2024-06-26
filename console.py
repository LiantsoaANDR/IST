import cmd
from models.base_model import BaseModel
from models.appareil import Appareil
from models.salle import Salle
from models import storage

def is_float(value):
    """Vérifie si value peut être convertie en float"""
    try:
        float(value)
        return True
    except ValueError:
        return False

class Shell(cmd.Cmd):

    class_list = ["BaseModel", "Appareil", "Salle"]

    prompt = '(estimateur) '
    
    def do_print(self, arg):
        """Print arg"""
        print(arg)

    def help_print(self):
        """Print la documentation de print"""
        print("print <arg_1> : print arg_1")

    def do_quit(self, arg):
        """Quitte la console"""
        return True
    
    def help_quit(self):
        """Print la documentation de quit"""
        print("quit : Quitte la console")

    def emptyline(self):
        """Ne fait rien"""
        pass

    def do_create(self, arg):
        """
        Crée un objet de son choix
        """
        arg_list = arg.split()
        if arg == "":
            print("** Manque du nom de la classe **")
        elif arg not in self.class_list:
            print("** Cette classe n'existe pas **")
        else:
            obj = eval(arg)()
            obj.save()
            print(obj)

    def help_create(self):
        """Print la documentation de create"""
        print("create <arg_1> : Crée un objet de type arg_1")

    def do_show(self, arg):
        """
        Print la representation de l'objet basée sur le nom de la classe et son identifiant unique
        """
        arg_list = arg.split()
        if not arg_list:
            print("** Manque de l'identifiant **")
            return

        obj_id = arg_list[0]
        found_obj = None
        for obj in storage.all().values():
            if obj.id == obj_id:
                found_obj = obj
                break

        if found_obj is None:
            print("Objet avec l'ID '{}' n'a pas été trouvé.".format(obj_id))
        else:
            print(found_obj)

    def help_show(self):
        """Print la documentation de show"""
        print("show <id_1>: Montre la représentation de l'objet ayant pour identifiant id_1")

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
                print("Detruit")
                return
            print("** L'objet n'existe pas **")

    def help_destroy(self):
        """Print la documentation de destroy"""
        print("destroy <arg_1> <id_1>: Supprime un object selon son nom de classe arg_1 et son identifiant unique id_1")

    def do_all(self, arg):
        """
        Prints toutes les representations de tous les objects selon ou non leur nom de classe
        """
        if arg == "":
            for obj in storage.all().values():
                print(str(obj))
        elif arg in self.class_list:
            for obj in storage.all().values():
                if obj.__class__.__name__ == arg:
                    print(str(obj))
        else:
            print("** L'objet n'existe pas **")

    def help_all(self):
        """Print la documentation de all"""
        print("all <arg_1>: Prints toutes les representations de tous les objects selon ou non leur nom de classe arg_1. Si arg_1 n'est pas donné, print toutes les représentations de tous les objects existants")

    def do_update(self, arg):
        """
        Met à jour l'objet selon son nom de classeet et de son identifiant en ajoutant ou mettant à jour son attribute
        (Enregistre les changements effectués)
        """
        arg_list = arg.split(' ')
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
                obj = storage.all()[obj_key]
                attribute_name = arg_list[2]
                new_value = arg_list[3][1:-1]
                if attribute_name in ['cons', 'user']:
                    if not new_value.isdigit() and not is_float(new_value):
                        print("La valeur de l'attribut '{}' doit être un entier ou un nombre décimal.".format(attribute_name))
                        return
                    
                setattr(obj, attribute_name, new_value)
                storage.save()
                print("Mise à jour de l'attribut '{}' de l'objet {} avec la valeur {}.".format(attribute_name, obj_key, new_value))
            else:
                print("** L'objet n'existe pas **")

    def help_update(self):
        """Print la documentation de update"""
        print("update <arg_1> <id_1> <arg_2> <arg_3>: Met à jour l'attribut arg_2 par la valeur arg_3 de l'objet de type arg_1 d'indentifiant id_1")

    def do_estimate(self, arg):
        """
        Fait une estimation de la consommation moyenne des utilisateurs
        """
        estim = 0.0
        if arg == "":
            for obj in storage.all().values():
                estim += float(obj.cons) * float(obj.user)
            print("La consommation totale de tout le systeme est : {:.2f} L".format(estim))
        elif arg in self.class_list:
            for obj in storage.all().values():
                if obj.__class__.__name__ == arg:
                    estim += float(obj.cons) * float(obj.user)
            print("La consommation totale de tous les '{}' est : {:.2f} L".format(arg, estim))
        else:
            print("** L'objet n'existe pas **")

    def help_estimate(self):
        """Print la documentation de estimate"""
        print("estimate <arg_1>: Print une estimation de la consommation en eau de arg_1 des utilisateurs. Si arg_1 n'est pas donné, print la consommation totales de tous le système")

    def do_precise(self, arg):
        """
        Fait un calcul de la consommation des appareils et/ou salles précisés
        """
        arg_list = arg.split()
        if not arg_list:
            print("** Manque de l'identifiant **")
            return

        total_conso = 0.0
        for obj_id in arg_list:
            found_obj = None
            for obj in storage.all().values():
                if obj.id == obj_id:
                    found_obj = obj
                    break

            if found_obj is None:
                print("Objet avec l'ID '{}' n'a pas été trouvé.".format(obj_id))
                return
            else:
                conso = float(found_obj.cons) * float(found_obj.user)
                total_conso += conso
        print("La consommation totale des objets précisés est : {:.2f} L".format(total_conso))

    def help_precise(self):
        """Print la documentation de precise"""
        print("precise <id_1> <id_2> <id_3> ...: Print une estimation de la consommation en eau des objets ayants pour id : id_1, id_2, ... (effectue une somme la consommation de ces objets)")


if __name__ == '__main__':
    Shell().cmdloop()