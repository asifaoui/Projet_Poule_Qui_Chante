'''
Module Parcourir.py
'''
import numpy as np
import pandas as pd



# fonction qui renvoie la première valeur non-NaN en parcourant les colonnes de gauche à droite
def first_valid_value_from_left(row):
    for v in row[::1]:               # parcourt les valeurs en commençant par la dexième colonne colonne
        if pd.notna(v) and str(v).strip() != '':
            return v
    return np.nan

# fonction qui renvoie la dernière valeur non-NaN en parcourant les colonnes de droite à gauche
def last_valid_value_from_right(row):
    for v in row[::-1]:               # parcourt les valeurs en commençant par la dernière colonne
        if pd.notna(v) and str(v).strip() != '':
            return v
    return np.nan