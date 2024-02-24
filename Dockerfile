FROM python:3

# Définition des variables d'environnement
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copie des fichiers nécessaires
COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app

# Définition du répertoire de travail
WORKDIR /app

# Exposer le port 8000
EXPOSE 8000

# Installation des dépendances Python
RUN pip install -r /tmp/requirements.txt

# Ajout d'un utilisateur sans répertoire home et sans mot de passe
RUN useradd -r -s /bin/false appuser

# Définition de l'utilisateur par défaut pour l'exécution du conteneur
USER appuser
