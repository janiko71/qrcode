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
* Pour la photo : `raspistill -o nom_fichier.jpg`
* Pour la vidéo : `raspivid -o nom_fichier.mp4`

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
### Installation de QRCode
1. Télécharger les sources sur PyPi.org (https://pypi.org/project/qrcode/#files)
1. Dézipper les fichiers et se rendre dans le répertoire obtenu
1. Lancer la commande `sudo python3 setup.py install` 
### Installation de pyzbar
1. Télécharger les sources sur PyPi.org (https://pypi.org/project/pyzbar/#files)
1. S'il n'y a que des fichiers de type `.whl`, alors il faut lancer la commande :

  `sudo pip3 install pyzbar-x.x.x-none-any.whl`
  
# Autres références
* https://pillow.readthedocs.io/en/3.1.x/reference/Image.html
