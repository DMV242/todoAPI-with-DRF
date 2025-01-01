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

# Installation des dépendances système
RUN apt-get update && \
    apt-get install -y python3-venv && \
    rm -rf /var/lib/apt/lists/*

# Création et activation de l'environnement virtuel
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Installation des dépendances Python dans l'environnement virtuel
RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt

# Ajout d'un utilisateur sans répertoire home et sans mot de passe
RUN useradd -r -s /bin/false appuser

# Définition de l'utilisateur par défaut pour l'exécution du conteneur
USER appuser

CMD ["python3","manage.py","runserver"]
