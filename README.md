# qrcode
Test de lecture et de transformation d'un QR Code (pour une utilisation avec Google Authenticator), dans le but de modifier le libellé affiché et faciliter son usage.
L'objectif est d'avoir un boîtier capable de lire un QR Code tout en étant *déconnecté* d'internet ! 
## Matériel utilisé
* Un Raspberry Pi 3 modèle B+
* Une caméra v2 officielle
# Installation
## Installation de l'OS
Je suis parti d'une installation Noobs simple (donc Raspbian), sans aucune option particulière. Cette installation contiendra de nombreux packages et modules inutiles, qu'on peut enlever aisément.
## Installation de la caméra
Il suffit de suivre le [tutoriel officiel](https://projects.raspberrypi.org/en/projects/getting-started-with-picamera).
Une fois la connexion réalisée, il faut tester la caméra, avec les commandes suivantes :
* Pour la photo : `raspistill -o _nom_fichier_.jpg`
* Pour la vidéo : `raspivid -o _nom_fichier_.mp4`

Par défaut, une vidéo de 5 secondes sera enregistrée. L'ensemble de paramètres utilisables est décrit ici :
* https://www.raspberrypi.org/documentation/raspbian/applications/camera.md

__Point important__ : la mise-au-point sur la caméra est manuelle ! Les dernières versions de la caméra sont livrées avec un outil pour faire la mise au point : il faut le placer sur l'objectif et tourner jusqu'à ce que ça convienne. 
## Pré-requis logiciel (Raspberry pi, armhf)
1. Modules python/PIP3
* pillow (PIL)
* pyzbar
* ~~zbar~~
* qrcode
2. Packages (sur Ubuntu)
* python3-pil
* zbar-tools 
* ~~python-zbar~~
* libzbar-dev (?)
