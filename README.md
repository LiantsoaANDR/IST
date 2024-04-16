# Logiciel de calcul
Projet estimateur de consommation en eau en fonction des utilisateurs

## Les commandes de notre console:
* print <abc>: print abc
* quit: Quitte la console
* create <abc>: Crée un objet de type abc
* show <id>: Montre la représentation de l'objet ayant pour identifiant id
* destroy <abc> <id>: Supprime un object selon son nom de classe abc et son identifiant unique id
* all <abc>: Prints toutes les representations de tous les objects selon ou non leur nom de classe abc. Si abc n'est pas donné, print toutes les représentations de tous les objects existants
* update <abc> <id> <ijk> <xyz>: Met à jour l'attribut ijk par la valeur xyz de l'objet de type abc d'indentifiant id
* estimate <abc>: Print une estimation de la consommation en eau de abc des utilisateurs. Si abc n'est pas donné, print la consommation totales de tous le système.
* precise <id_1> <id_2> <id_3> ...: Print une estimation de la consommation en eau des objets ayants pour id : id_1, id_2, ... (effectue une somme la consommation de ces objets)