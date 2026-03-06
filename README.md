# Étude de Marché : Internationalisation des Ventes de Poulets Bio

Ce projet s'inscrit dans une démarche de conseil stratégique pour une entreprise souhaitant étendre ses activités à l'international. L'objectif est d'identifier les pays les plus prometteurs pour l'exportation de produits avicoles biologiques à l'aide de méthodes statistiques avancées.

# Objectifs du Projet:
**Collecte et Nettoyage :** Consolidation de données provenant de sources internationales (FAO, Banque Mondiale) pour constituer un jeu de données fiable.

**Analyse Exploratoire :** Analyse multivariée pour comprendre les corrélations entre les variables économiques et démographiques.

**Segmentation de Marché :** Groupement des pays par similarités afin d'isoler des zones d'opportunités.
**Recommandations :** Sélection d'un "cluster" cible et justification de la stratégie d'implantation.

## Stack Technique & Méthodologie

**Langage :** Python (Pandas, Numpy, Matplotlib, Seaborn). 
**Réduction de dimension :** **Analyse en Composantes Principales (ACP)** pour synthétiser l'information.
**Clustering (Apprentissage non supervisé) :** * **Classification Ascendante Hiérarchique (CAH)** avec visualisation par dendrogramme.

**K-means** pour stabiliser et affiner la segmentation.

## 📁 Organisation du Répertoire

`data/` : Jeux de données bruts et nettoyés.

`Preparation_data/` : Préparation et analyse complète sous **Jupyter/Google Colab** détaillant chaque étape du processus.

'Fusion_data/` : Fusion des données.
 `Clustering/` : Classification des pays suivant des algorithmes.

## Résultats Clés

L'analyse a permis d'identifier **4** groupes de pays distincts. Le cluster numéro 3  présente un fort pouvoir d'achat allié à une croissance constante de la consommation de viande, ce qui en fait la cible prioritaire pour l'exportation.
