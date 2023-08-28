def stats_Bookings():
    
    # Import des bibliothèques utiles
    import pandas as pd
    import numpy as np
    from datetime import datetime

    # Lecture du fichier bookings.csv
    df = pd.read_csv("~/csvFile/bookings.csv")

    # Nettoyage du format de la colonne amount 
    def clean_amount(amount):
        symbols_to_remove = {'£', '€', '$'}
        cleaned_item = ''.join(char for char in amount if char not in symbols_to_remove)
        cleaned_item = cleaned_item.replace(',', '.').strip()
        return round(float(cleaned_item),2)

    df['amount'] = np.vectorize(clean_amount)(df['amount'])

    # Normalisation du format des dates YYYY_MM
    def clean_Date(date):
        if '/' in date:
            date_obj = datetime.strptime(date, '%d/%m/%Y')
        elif '-' in date:
            date_obj = datetime.strptime(date, '%d-%m-%Y')
        return date_obj.strftime('%Y_%m')
    
    df['month'] = np.vectorize(clean_Date)(df['date'])

    # Changement du booking_id en valeur de 1 pour calculer le number_of_bookings par mois
    df['number_of_bookings'] = df['booking_id'].apply(lambda booking: str(booking).replace(booking,'1'))
    df['number_of_bookings'] = df['number_of_bookings'].apply(lambda booking:int(booking))

    # Suppression des colonnes qui ne servent plus
    df = df.drop(['date','client_id','client_name','booking_id'], axis=1)
    
    # Changement de nom pour la colonne guests
    df.rename(columns={'guests':'number_of_guests'}, inplace=True)
    
    # Création d'un nouveau DataFrame à partir des colonnes nécessaire pour le nouveau CSV
    new_df = df[['restaurant_id', 'restaurant_name','country','month','number_of_bookings','number_of_guests','amount']]

    # Utilisation de groupby avec sum() pour calculer les éléments par année et par mois
    new_df = df.groupby(['restaurant_id','restaurant_name','country','month']).sum()
    
    # Chargement du nouveau DataFrame dans un csv
    new_df.to_csv('~/csvFile/monthly_restaurants_report.csv')