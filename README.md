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

