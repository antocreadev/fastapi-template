# --- Importation des modules
# sqlalchemy est utilisé pour la gestion de la base de données, cela permet de créer des modèles de données, de les manipuler, etc.
from sqlalchemy import Column, Integer, String, Boolean, ForeignKey
# sqlalchemy.orm est utilisé pour la session de la base de données, cela permet d'accéder à la base de données, de la lire et de l'écrire, etc.
from sqlalchemy.orm import relationship
# sqlalchemy.ext.declarative est utilisé pour la déclaration de la base de données
from database import Base

# --- User model
class User(Base):
    __tablename__ = "Users"
    id = Column(Integer, primary_key=True, index=True)
    firstname = Column(String)
    lastname = Column(String)
    email = Column(String, unique=True, index=True)
    password = Column(String) 
    rgpd = Column(Boolean)