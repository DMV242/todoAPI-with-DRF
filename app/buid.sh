#!/bin/bash

# Mettre à jour la liste des paquets
apt-get update

# Installer les dépendances requises
apt-get install -y build-essential libsqlite3-dev libgeos-dev \
    libproj-dev libxml2-dev libjson-c-dev libcurl4-gnutls-dev \
    libpng-dev libtiff-dev libjpeg-dev

# Installer GDAL
apt-get install -y gdal-bin libgdal-dev python3-gdal

# Vérification de l'installation
echo "GDAL version:"
gdalinfo --version

# Installation des dépendances Python
pip install -r ../requirements.txt

echo "Installation terminée avec succès."
