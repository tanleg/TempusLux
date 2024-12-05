Ce projet est réalisé dans le cadre d’un cours sur la prompt ingénierie, consacré à l’utilisation des IA génératives.
L’objectif était de créer un site e-commerce dédié à la vente de montres haut de gamme, en moins de 3 heures, grâce à l’assistance de ces outils.
Il est important de préciser que je n’ai écrit aucune ligne de code pour ce projet : chaque fonctionnalité, design, et composant du site (y compris le README) a été généré ou rédigé par une intelligence artificielle, démontrant la puissance et l’efficacité de ces technologies dans le développement web moderne.


# Tempus Lux - E-commerce pour Montres de Luxe
Tempus Lux est une application web dédiée à la vente de montres haut de gamme. Elle se compose d'une API REST, développée avec FastAPI, et d'un client web, développé avec Flask, permettant de naviguer et consulter les détails des montres disponibles.

## Fonctionnalités
- Liste des montres : Affichage de toutes les montres disponibles à la vente.
- Détails d'une montre : Consultation des caractéristiques détaillées d'une montre.
- CRUD via API : Gestion des montres, marques et catégories à travers l'API REST.

## Technologies utilisées
### Backend
- Python 3.12
- FastAPI : API REST performante et moderne.
- SQLAlchemy : ORM pour la gestion de la base de données.
- MySQL : Base de données relationnelle.
### Frontend
- Flask : Framework léger pour le client web.
- Bootstrap : Framework CSS pour le style.
### Installation
1. Pré-requis
- Python 3.10+
- MySQL ou un autre serveur de base de données compatible avec SQLAlchemy
- Git
2. Cloner le dépôt
```git clone https://github.com/tanleg/TempusLux.git```
```cd TempusLux```
3. Configuration de l'environnement
#### Backend
- Créez un environnement virtuel :
```python -m venv venv```
```venv\Scripts\activate``` (Windows)
- Installez les dépendances :
```pip install -r requirements.txt```
- Configurez la base de données dans database.py :
```DATABASE_URL = "mysql+pymysql://username:password@localhost/tempus_lux"```
- Créez les tables dans la base :
```python -m database```
- Lancez le serveur FastAPI :
```uvicorn main:app --reload```
#### Frontend
- Configurez le client Flask :
Modifiez app.py pour pointer vers l'URL de l'API FastAPI (API_URL).
- Lancez l'application Flask :
```python app.py```
- Accédez à l'application :
Liste des montres : http://127.0.0.1:5000
