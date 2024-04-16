# Logiciel de calcul
Projet estimateur de consommation en eau en fonction des utilisateurs

## Les commandes du console:
* print <x>: print x
* quit: Quitte la console
* create <x>: Crée un objet de type x
* show <id>: Montre la représentation de l'objet ayant pour identifiant id
* destroy <x> <id>: Supprime un object selon son nom de classe x et son identifiant unique id
* all <x>: Prints toutes les representations de tous les objects selon ou non leur nom de classe x. Si x n'est pas donné, print toutes les représentations de tous les objects existants
* update <x> <id> <y> <z>: Met à jour l'attribut y par la valeur z de l'objet de type x d'indentifiant id
* estimate <x>: Print une estimation de la consommation en eau de x des utilisateurs. Si x n'est pas donné, print la consommation totales de tous le système.
* precise <id_1> <id_2> <id_3> ...: Print une estimation de la consommation en eau des objets ayants pour id : id_1, id_2, ... (effectue une somme la consommation de ces objets)