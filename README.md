# Rapport 

Tout les flake Sucess 
Deux test ne passe pas sur tout les tests


## Installation

Suivez ces étapes pour mettre en place l'environnement de développement :

1. Clonez le dépôt :

```sh
git clone https://github.com/8astien/OCR_P4/tree/main
cd OCR_P4
```


2. Activez l'environnement virtuel :

Sur Windows :

```sh
env\Scripts\activate
```

Sur Unix ou MacOS :

```sh
source env/bin/activate
```


## Exécution du Programme

Pour démarrer l'application, exécutez :

```sh
python main.py
```

3. Effectuer les  tout les tests : 

```
 --python -m unittest discover -s tests    
```



## Génération du Rapport flake8-html

Pour générer un rapport de conformité du code avec flake8-html, exécutez la commande suivante :

```sh
flake8 --format=html --htmldir=rapport_flake8
```

Ouvrez `rapport_flake8/index.html` dans votre navigateur pour voir le rapport.

# Partiels_Python
# Partiels_Python



