# Introduction
[Lien du dataset](https://www.kaggle.com/datasets/austinreese/craigslist-carstrucks-data?select=vehicles.csv)
### Objectif :
Prédire le prix d'une voiture d'occasion en fonction de plusieurs paramètres (année, manufactureur, model, condition, type carburant, kilométrage, transmission, couleur)
### Technologies : 
- Pandas
- Numpy
- Matplotlib
- Sklearn

### Problème rencontré : 
- Score de prédiction faible -> Plus on donnait de données à notre modèle, moins il était performant
### Solution trouvée :
- Nettoyer le dataset
    - Supprimer les entrées qui contiennent des caractéristiques nulles
    - Supprimer les entrées qui contiennent des valeurs abérrantes (exemple : prix à 5€ avec état neuf)
- Tester différents modèles
    - Régression linéaire
    - Régression polynomiale
    - Arbre de décision
    - Forêt d'arbres décisionnel
### Améliorations possible : 
- Nettoyer encore plus le dataset
    - Beaucoup de voiture avec très peu de km (1, 2, 3...)
    - Enlever tous les doublons
    - Détecter et supprimer toutes les valeurs abérrantes (exemple : Lamborghini à 10000€)
    - Factoriser les mêmes modèles de voiture sous un même modèle (exemple : Toyota Prius V, Toyota Prius 5, Toyota V Prius etc... = Toyota Prius V)
- Tester d'autre modèles qu'on ne connait pas pour l'instant

    
---
