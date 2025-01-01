FROM python:3

# Définition des variables d'environnement
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Copie des fichiers nécessaires
COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app

# Définition du répertoire de travail
WORKDIR /app

# Exposer le port 8000 pour le serveur Django
EXPOSE 8000

# Installation des dépendances système nécessaires
RUN apt-get update && \
    apt-get install -y python3-venv && \
    rm -rf /var/lib/apt/lists/*

# Création et activation de l'environnement virtuel
RUN python3 -m venv /venv
ENV PATH="/venv/bin:$PATH"

# Installation des dépendances Python dans l'environnement virtuel
RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt

# Création et configuration d'un utilisateur non root
RUN useradd -r -s /usr/sbin/nologin appuser && \
    chown -R appuser:appuser /app

# Définition de l'utilisateur par défaut pour l'exécution du conteneur
USER appuser

# Commande par défaut
CMD ["python3", "manage.py", "runserver", "0.0.0.0:8000"]
