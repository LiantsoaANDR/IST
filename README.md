# Logiciel de calcul
Projet estimateur de consommation en eau en fonction des utilisateurs

## Les commandes de notre console:
* print <xxx>: print xxx
* quit: Quitte la console
* create <xxx>: Crée un objet de type xxx
* show <id>: Montre la représentation de l'objet ayant pour identifiant id
* destroy <xxx> <id>: Supprime un object selon son nom de classe xxx et son identifiant unique id
* all <xxx>: Prints toutes les representations de tous les objects selon ou non leur nom de classe xxx. Si xxx n'est pas donné, print toutes les représentations de tous les objects existants
* update <xxx> <id> <yyy> <zzz>: Met à jour l'attribut yyy par la valeur zzz de l'objet de type xxx d'indentifiant id
* estimate <xxx>: Print une estimation de la consommation en eau de xxx des utilisateurs. Si xxx n'est pas donné, print la consommation totales de tous le système.
* precise <id_1> <id_2> <id_3> ...: Print une estimation de la consommation en eau des objets ayants pour id : id_1, id_2, ... (effectue une somme la consommation de ces objets)