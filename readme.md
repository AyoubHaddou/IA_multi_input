# Modèle de deep learning multi-inputs

* * * * * * * *

Dans ce projet d'une semaine, on a developper un modèle de deep learning multi-inputs adapté dans une application streamlit.

# Context du projet: 

Vous êtes Data Scientist pour une startup "Les bonnes affaires" qui est une marketplace en ligne. Cette plateforme permet à des particuliers de vendre des produits. Pour l'instant, les vendeurs postent une description et une photo de leurs produits, puis ils choisissent eux-même une catégorie. Nos analyses montrent que cette approche est peu fiable et conduit à des produits qui sont mal-classifiés.

​

L'équipe de direction a décidé d'automatiser cette tâche. Pour cela, elle va s'appuyer sur le pôle Data dont vous faîtes parti. Le lead data scientist de votre équipe Sébastien, vous demande d'effectuer un proof of concept.

​

Votre mission est donc d'évaluer la faisabilité du projet.

​

Vous devez étudier 3 approches :

- Créer un modèle basé uniquement sur le texte des descriptions
- Créer un modèle basé uniquement sur les images
- Créer un modèle qui combine les images et le texte
​

Afin de réaliser ce travail vous disposez d'un échantillon de données comprenant 1050 articles avec description et images. Étant donné la nature des données, nous avons décidé de te fournir un nombre limité de données d'entraînement afin d'accélerer le temps d'entrainement. En effet, l'entreprise étant toujours une startup, elle doit maitriser ses coûts au maximum. Si votre étude de faisabilité s'avère prometeuse nous pourrons basculer sur un jeu de données bien plus volumineux.


# Tache à finir: 

A faire pour plus tard: 
- Sécuriser l'app 
- Ajouter des users 
- Limiter à 10 annonces par user (offre gratuite) 
- Ajoute une API pour le modèle 
- Déployer l'ensemble du projet
- Faire de la data augmentation dans le modele de computer vision (et/ou utilisé un modèle pré-entrainé et faire un transfert learning)


# Compléments: 
- Le modele s'est entrainé sur 1000 images. 
- L'étude de faisabilité semble positive, avec beaucoup plus d'images on pourrait prendre d'avantage de catégories


# Pour lancer l'application en local: 
- git pull https://github.com/AyoubHaddou/IA_multi_input
- pip install -r requirements.txt
- streamlit run app.py 
