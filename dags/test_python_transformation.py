import unittest
from datetime import datetime

# Déclaration de la fonction de test clean_amount
def clean_amount(amount):
    symbols_to_remove = {'£', '€', '$'}
    cleaned_item = ''.join(char for char in amount if char not in symbols_to_remove)
    cleaned_item = cleaned_item.replace(',', '.').strip()
    return round(float(cleaned_item),2)

# Déclaration de la fonction Date
def clean_Date(date):
    if '/' in date:
        date_obj = datetime.strptime(date, '%d/%m/%Y')
    elif '-' in date:
        date_obj = datetime.strptime(date, '%d-%m-%Y')
    return date_obj.strftime('%Y_%m')

# Tests unitaires sur clean amount
def test_clean_amount():
    assert clean_amount('€100.00') == 100.0
    assert clean_amount('$50.50') == 50.5
    assert clean_amount('£75,25') == 75.25
    assert clean_amount('27,25 £ ') == 27.25

# Tests unitaires sur clean Date
def test_clean_Date():
    assert clean_Date('12/03/2023') == '2023_03'
    assert clean_Date('15-06-2022') == '2022_06'


