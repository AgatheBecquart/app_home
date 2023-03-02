# Projet de prédiction des prix de l'immobilier

Ce projet vise à prédire le prix des biens immobiliers à partir d'un modèle de machine learning entraîné sur un ensemble de données. Les utilisateurs peuvent créer des prédictions en remplissant un formulaire avec les caractéristiques de leur bien immobilier. Les prédictions sont ensuite enregistrées dans une base de données pour permettre aux utilisateurs de les consulter, de les modifier ou de les supprimer.

## Développement de l'algorithme

J'ai choisi un modèle de régression Ridge pour prédire les prix immobiliers à partir de données de vente immobilières. 

Les étapes principales de l'algorithme sont :

Diviser les données en ensembles de formation et de test à l'aide de train_test_split.
Créer un pipeline de prétraitement pour les variables numériques en appliquant une transformation polynomiale de degré 2 et une mise à l'échelle MinMax avec PolynomialFeatures et MinMaxScaler de la bibliothèque Scikit-learn.
Créer un pré-processeur pour les variables catégorielles en appliquant une encodage One-Hot avec OneHotEncoder de la bibliothèque Scikit-learn.
Utiliser ColumnTransformer pour appliquer le pré-traitement à chaque type de variable.
Définir un modèle de régression Ridge avec une valeur d'alpha de 1.
Créer un pipeline final qui applique le prétraitement et la régression Ridge avec Pipeline.
Entraîner le modèle sur les données d'entraînement avec la méthode fit du pipeline final.
Évaluer la performance du modèle sur les données de test avec la méthode score du pipeline final.

## Installation
Clonez ce dépôt de code sur votre machine locale.
Installez les dépendances avec pip install -r requirements.txt.
Configurez la base de données en modifiant le fichier settings.py avec vos informations de connexion.
Créez les tables de la base de données avec python manage.py migrate.
Créez un superutilisateur avec python manage.py createsuperuser.

## Utilisation
Lancez le serveur web avec python manage.py runserver.
Accédez à l'application dans votre navigateur à l'adresse http://localhost:8000/.
Créez une prédiction en remplissant le formulaire sur la page d'accueil.
Consultez vos prédictions sur la page de consultation.
Modifiez ou supprimez vos prédictions en cliquant sur les liens correspondants.

## Architecture
Le projet est organisé en différentes vues qui gèrent les interactions avec l'utilisateur :

estimate: affiche le formulaire de création de prédiction.
prediction_detail: affiche les détails d'une prédiction existante.
prediction_change: permet à l'utilisateur de modifier une prédiction existante.
prediction_delete: permet à l'utilisateur de supprimer une prédiction existante.
Ces vues sont liées aux modèles de données Prediction et UserProfile qui définissent les champs et les relations de la base de données. Les formulaires sont définis dans le fichier forms.py.


## Contribuer
Les contributions sont les bienvenues ! Si vous souhaitez contribuer à ce projet, veuillez ouvrir une issue ou une pull request avec votre proposition.