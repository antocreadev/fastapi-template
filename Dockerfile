# Utilise une image Python officielle
FROM python:3.10

# Définit le répertoire de travail à l'intérieur du conteneur
WORKDIR /code

# Copie uniquement les fichiers nécessaires pour installer les dépendances
COPY ./requirements.txt /code/requirements.txt

# Installe les dépendances sans mise en cache
RUN pip install --no-cache-dir --upgrade -r /code/requirements.txt

# Copie le code source dans l'image (utile pour éviter les problèmes si le volume monté ne fonctionne pas)
COPY . /code

# Commande pour lancer le serveur FastAPI en mode développement
CMD ["uvicorn", "src.main:app", "--host", "0.0.0.0", "--port", "8090", "--reload"]
