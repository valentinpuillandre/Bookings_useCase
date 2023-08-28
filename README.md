## DAG Airflow pour le Traitement de Données et l'Intégration PostgreSQL

##### Ce référentiel contient un exemple d'utilisation d'Apache Airflow pour automatiser le traitement de données, la transformation et l'intégration avec une base de données PostgreSQL. La DAG fournie effectue les tâches suivantes :


1. Vérification de l'Existence du Fichier : Vérifie l'existence du fichier CSV d'entrée contenant les données de réservation.

2. Transformation des Données : Applique le nettoyage et la transformation des données à l'aide d'une fonction Python.

3. Vérification de l'Existence du Fichier Transformé : Vérifie l'existence du fichier CSV transformé.

4. Création de la Table PostgreSQL : Crée une table nommée bookings dans la base de données PostgreSQL.

5. Insertion des Données dans PostgreSQL : Insère les données transformées du fichier CSV dans la table bookings.


#### Prérequis

Docker et Docker Compose doivent être installés sur votre système.

Clonez ce référentiel sur votre machine locale : https://github.com/valentinpuillandre/Bookings_useCase.git

Ouvrez Powershell et aller dans le chemin du dossier cloné.

Tapez la commande suivante : docker-compose -f .\docker-compose-LocalExecutor.yml up -d

#### Connexion à Airflow

lien de connexion : http://localhost:8080/admin/

#### Connexion à pgAdmin

lien de connexion : http://localhost:5050/login?next=%2F

    -   UserName : admin@admin.com
    -   Password : root

##### Ajouter une connexion au serveur postgres sur pgAdmin /

    -   Cliquez sur "Add New Server"
    -   Donnez un Name à la connexion (exemple : test_db)
    -   Allez dans l'onglet "Connection" : Ajoutez l'IP en référence à postgresql
        -   Dans powershell ajoutez le commande : docker container ls
        -   récupérez l'ID de postgres (exemple : f12292a2fefvg )
        -   Copiez cette valeur puis collez-la dans la commande : docker inspect f12292a2fefvg
        -   Récupérez l'IP à la ligne : "IPAddress" (exemple : "172.21.0.2") 

#### Dans AirFlow 

    -   2 DAG présentes :
        -   test_dag.py : tests unitaires
        -   UseCase : correspondant à la DAG pour le use Case Bookings


