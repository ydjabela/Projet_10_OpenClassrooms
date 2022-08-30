# Projet_10_OpenClassrooms
## Créez une API sécurisée RESTful en utilisant Django REST
SoftDesk, une société d'édition de logiciels de développement et de collaboration, a décidé de publier une application permettant de remonter et suivre des problèmes techniques (issue tracking system). Cette solution s’adresse à des entreprises clientes, en B2B. 

###Description du projet :


### Récupérer le projet :

```
git clone https://github.com/ydjabela/Projet_10_Openclassrooms
```

### Création de l'environnement virtuel

Assurez-vous d'avoir installé python et de pouvoir y accéder via votre terminal, en ligne de commande.

Si ce n'est pas le cas : https://www.python.org/downloads/

```
python -m venv Projet_10
```

### Activation de l'environnement virtuel du projet

Windows :

```
Projet_10\Scripts\activate.bat
```

MacOS/Linux :
```
source Projet_9/bin/activate
```

### Installation des packages necessaire pour ce projet
```
pip install -r requirements.txt
```

### Fonctionnement:
Une fois activé, pour démarrer le serveur local, il faudra utiliser la commande :
```
python manage.py runserver 
```
### Postman documentation

#### Cette commande sera obligatoire à chaque fois que vous voudrez travailler avec le cours. Dans le même terminal, tapez maintenant
```
pip install -r requirements.txt
```
###Vérifier la qualité du code :
Pour lancer la vérification de la qualité du code : 
```
flake8 --format=html --htmldir=flake-report --exclude=env --max-line-length=119
```
### Contributeurs
- Yacine Djabela
- Stephane Didier

