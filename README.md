# Logiciel de calcul
Projet estimateur de consommation en eau en fonction des utilisateurs

# Autheurs:
ANDRIANAMBININA Liantsoa 				GSI-MP	N°02
RAKOTOMALALA Andry Ambinintsoa 			GSI-ER 	N°09
RAKOTOMAVO Finaritra Vola				GSI-ER 	N°10

## Les commandes de notre console:
* print <arg_1>: print arg_1
* quit: Quitte la console
* create <arg_1>: Crée un objet de type arg_1
* show <id>: Montre la représentation de l'objet ayant pour identifiant id
* destroy <arg_1> <id>: Supprime un object selon son nom de classe arg_1 et son identifiant unique id
* all <arg_1>: Prints toutes les representations de tous les objects selon ou non leur nom de classe arg_1. Si arg_1 n'est pas donné, print toutes les représentations de tous les objects existants
* update <arg_1> <id> <arg_2> <arg_3>: Met à jour l'attribut arg_2 par la valeur arg_3 de l'objet de type arg_1 d'indentifiant id
* estimate <arg_1>: Print une estimation de la consommation en eau de arg_1 des utilisateurs. Si arg_1 n'est pas donné, print la consommation totales de tous le système.
* precise <id_1> <id_2> <id_3> ...: Print une estimation de la consommation en eau des objets ayants pour id : id_1, id_2, ... (effectue une somme la consommation de ces objets)