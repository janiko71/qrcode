# qrcode
Test de lecture et de transformation d'un QR Code (pour une utilisation avec Google Authenticator), dans le but de modifier le libellé affiché et faciliter son usage.
L'objectif est d'avoir un boîtier capable de lire un QR Code tout en étant *déconnecté* d'internet ! 
## Matériel utilisé
* Un Raspberry Pi 3 modèle B+
* Une caméra v2 officielle
# Installation
## Installation de l'OS
* Je suis parti d'une installation Noobs simple (donc Raspbian), sans aucune option particulière. Cette installation contiendra de nombreux packages et modules inutiles, qu'on peut enlever aisément.
## Installation de la caméra
Il suffit de suivre le [tutoriel officiel](https://www.raspberrypi.org/documentation/raspbian/applications/camera.md).
## Pré-requis testé sur raspberry pi (armhf)
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
