
 ###########################################################################################
 #Une application de gestion de stock ou inventaire avec python et xml comme base de donnée#
 ###########################################################################################

I)Structure du projet:

*Examen_xml (dosscier racine)
 *data (les donnee xml utiliser)
|-dataFournisseur.xml (ici les donnée fournisseur sont  stocke)
|-dataProduit.xml(ici les donnée produit sont  stocke)
|-fournisseurSchema.xsd
|-produitSchema.xsd
 *env (l'environement virtuelle)
 *icone (les icone utiliser dans le projet)
 |-gui_support.py (logique du projet)
 |-gui.py (view du projet ou interface utilisateur)
 *Readme.txt (Structure du projet et explication du lancement de l'application)
 *requirements.txt (les dépendance neccesaire pour faire fonctionner le projet correctement avec les bonne versions)

II)Pres-requis:
 -python 3.12.8 (supérieur ou égale) installer dans votre oridinateur: pour teste la version du python avec la commande: "python --version" ou "python3 --version" selon la version de
votre python.
 - un system d'exploitation windows 10 ou 11
 -le code source du projet( place dans votre disque D:\) 

III)Pour démarer l'application il faut suivre attentivement ces étape ci-dessous:

 Etape 1- ouvrire le CMD de windows (tapezsur le bouton demarer + R -> tapez CMD -> tapez executer ou entrer)

 Etape 2- navigé vers le projet et activée l'environement virtuelle:

     Faire c'est commande étape par étape dans le cmd (et apres chaque commande il faut appuyer sur le bouton Entre):
     1) d:
     2) cd Examen_xml (se deplace dans le projet)
     3) env\Scripts\activate (activation de l'environement virtuelle)

 Etape 3- Une fois l'environement virtuelle lance vous aurais : (env) D:\Examen_xml> si vous n'arais pas cette resulat re faire l'étape 2

 Etape 4- lance le projet avec la commande selon la version de votre python:

       python gui_support.py 
                ou
       python3 gui_support.py

 Etape 5: Attendre un instant que le projet démarer , sinon  veuiller refaire les étapes de 1 à 5 ou bien  lire le Remarque au ci-dessous!.

#########################
#Remarque trés important#
#########################

Si le projet demarer mais rien ne fonctionner vous donc il faut installer les dépendance qui se trouve dans le fichier requirements.txt 
Il faut avoire une connexion stable: et activée l'environement virtuelle et lance cette commande : "pip install -r requirements.txt"
Sa va télècharger les dépendance néccesaire pour bien fonctionner le projet.
exemple:
-(env) D:\Examen_xml> pip install -r requirements.txt

Et attendre que le télèchargement se finisent bien et relance le projet ou refaire les 5 étapes pour démarer l'application.
