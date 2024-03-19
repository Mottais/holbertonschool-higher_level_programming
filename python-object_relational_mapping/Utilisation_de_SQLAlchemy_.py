#!/usr/bin/python3
"""Module joining 2 tables"""
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

# Création d'une instance de moteur SQLAlchemy pour se connecter à la base de données MySQL
# Remplacez 'mysql+mysqldb://username:password@host:port/Ma_BD' avec vos propres informations de connexion
# Assurez-vous que la base de données 'Ma_BD' existe déjà sur votre serveur MySQL.
# engine = create_engine('mysql+mysqldb://username:password@host:port/Ma_BD', echo=True)
# exemple sur un serveur :
# engine = create_engine('mysql+mysqldb://root:rout@192.168.1.100:3306/Ma_BD', echo=True)
# exemple sur un serveur avec nom de domaine :
# engine = create_engine('mysql+mysqldb://root:root@mysql.example.com:3306/Ma_BD', echo=True)
# Si  base de données MySQL est hébergée localement sur votre propre machine, connexion avec l'adresse localhost ou 127.0.0.1
engine = create_engine('mysql+mysqldb://root:root@localhost:3306/Ma_BD', echo=True)


Base = declarative_base()


# Définition d'une classe de modèle pour notre table 'utilisateurs'
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String(50))
    age = Column(Integer)


# Création de la table dans la base de données
Base.metadata.create_all(engine)

# Création d'une session pour interagir avec la base de données
Session = sessionmaker(bind=engine)
session = Session()

# Création de quelques instances d'utilisateur et insertion dans la base de données
user1 = User(name='Alice', age=30)
user2 = User(name='Bob', age=25)

session.add(user1)
session.add(user2)
session.commit()

# Récupération des utilisateurs de la base de données
users = session.query(User).all()

# Affichage des utilisateurs
print('id name age')
for user in users:
    print(user.id,'', user.name, user.age)

# Fermeture de la session
session.close()
