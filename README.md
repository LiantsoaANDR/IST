# Logiciel de calcul
Projet estimateur de consommation en eau en fonction des utilisateurs

# Auteurs:
- ANDRIANAMBININA Liantsoa 				GSI-MP	N°02
- RAKOTOMALALA Andry Ambinintsoa 		GSI-ER 	N°09
- RAKOTOMAVO Finaritra Vola				GSI-ER 	N°10

## Utilisation
Pour utiliser l'outil, il faut télécharger le répertoire "IST" puis lancer "console.py".

## Les commandes de notre console:
* print <arg_1>: print arg_1
* quit: Quitte la console
* create <arg_1>: Crée un objet de type arg_1
* show <id_1>: Montre la représentation de l'objet ayant pour identifiant id_1
* destroy <arg_1> <id_1>: Supprime un object selon son nom de classe arg_1 et son identifiant unique id_1
* all <arg_1>: Prints toutes les representations de tous les objects selon ou non leur nom de classe arg_1. Si arg_1 n'est pas donné, print toutes les représentations de tous les objects existants
* update <arg_1> <id_1> <arg_2> <arg_3>: Met à jour l'attribut arg_2 par la valeur arg_3 de l'objet de type arg_1 d'indentifiant id_1. La valeur arg_3 doit être entre "" (de la forme "arg_3").
* estimate <arg_1>: Print une estimation de la consommation en eau de arg_1 des utilisateurs. Si arg_1 n'est pas donné, print la consommation totales de tous le système.
* precise <id_1> <id_2> <id_3> ...: Print une estimation de la consommation en eau des objets ayants pour id : id_1, id_2, ... (effectue une somme la consommation de ces objets)
* help <un_des_cmd> : Print la docummentation de un_des_cmd (Exemple: help update)