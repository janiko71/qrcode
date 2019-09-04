# Imports pour les QR Codes
import re
import qrcode
import pprint
from pyzbar.pyzbar import decode
from PIL import Image, ImageFile
import urllib.parse
import csv

# Imports pour l'application "console"
from prompt_toolkit import Application, prompt, print_formatted_text, HTML
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.enums import DEFAULT_BUFFER
from prompt_toolkit.styles import Style
from prompt_toolkit.application import get_app
from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit.widgets import Frame, Box, Button, TextArea, RadioList
from prompt_toolkit.shortcuts import yes_no_dialog, PromptSession

from prompt_toolkit.layout import NumberedMargin, ScrollOffsets, WindowAlign
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.layout.containers import Window, FloatContainer, Float, HSplit, VSplit
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl
from prompt_toolkit.layout.screen import Screen
from prompt_toolkit.layout.dimension import D



#
# Constantes et variables globales
#

QR_REGEX = r"(otpauth:\/\/totp\/)(.+)(:)(.+)(\?secret=)([A-Z0-9]{64})(\&issuer\=)(.+)"
FIRST_LINE = ["identifiant", "mail", "secret", "issuer", "otp"]


# ==================================================================================
#
#   Classe QR Code (pour faciliter leur manipulation)
#
# ==================================================================================

class QRCode:

    # 
    # Cette classe implémente un objet QR Code de type Google Authenticator. 
    #
    # Un objet est instancié à partir de la chaîne de caractère composant le QR Code passée en paramètre lors de la création.
    #
    # Exemple que QR Code brut : otpauth://totp/Amazon%20Web%20Services:user@itim-srotest-sbx?secret=5Z...GG&issuer=Amazon%20Web%20Services
    #

    def __init__(self, s):

        # On parse la chaîne 
        res = re.match(QR_REGEX, s)

        # On suppose que les informations sont bien formées :)
        try:    
            self.identifiant = res.group(2)
            self.user = res.group(4)
            self.secret = res.group(6)
            self.issuer = res.group(8)
            self.otp = s
        except Exception as e:            
            print("Erreur lors de l'interprétation d'un enregistrement")
            print("Erreur rencontrée : " + str(e))

    def verifier(qr, ch):
        pass

    def __str__(self):
        #
        # Affichage d'une instance
        #
        return "id({}) user({}) issuer({})".format(self.identifiant, self.user, self.issuer)

    def to_csv(self):
        #
        # Retourne le QR Code sous forme utilisable en CSV
        #
        res = []
        res.append(self.identifiant)
        res.append(self.user)
        res.append(self.secret)
        res.append(self.issuer)
        res.append(self.otp)
        return res


# ==================================================================================
#
#   Fonctions pour le fichier des QR Codes
#
# ==================================================================================

def lecture_QR():

    #
    # Lecture du fichier des QR Codes
    # 
    # Format : CSV avec séparateur ';'
    #
    # Le fichier contient dans l'ordre :
    #
    #   1/ Identifiant
    #   2/ Utilisateur (associé au QR Code)
    #   3/ _the_ secret
    #   4/ Issuer (émetteur, propriétaire)
    #
    # La 1ère ligne comprend la description des colonnes
    #

    liste_qr = []    

    with open('test_in.csv', 'r', newline='') as csvfile:
        csvreader = csv.reader(csvfile, dialect = csv.excel, delimiter = ';')
        for qr in csvreader:
            line_num = csvreader.line_num
            if (line_num > 1):
                qrc = QRCode(qr[4])
                # debug : print(qrc)
                liste_qr.append(qrc)

    return liste_qr


def ecriture_QR(lst):

    #
    # Ecriture du fichier des QR Codes (on n'écrit que les QR Codes des comptes racines)
    #

    with open('test_out.csv', 'w', newline='') as csvfile:
        csvwriter = csv.writer(csvfile, dialect = csv.excel, delimiter = ';')
        csvwriter.writerow(FIRST_LINE)
        for qr in lst:
            csvwriter.writerow(qr.to_csv())



inputImage = Image.open("test.jpg")
infos = decode(inputImage)
b_txt = infos[0][0].replace(b'\n',b'')
txt = b_txt.decode()
"""print(txt)
print()"""

regle = r"(otpauth:\/\/totp\/)(.+)(:)(.+)(\?secret=)([A-Z0-9]{64})(\&issuer\=)(.+)"
res = re.match(regle, txt)

"""for i in range(0, res.lastindex + 1):
    print(str(i) + " " + res.group(i))"""

"""qr_identifiant = res.group(2)
qr_user = res.group(4)
qr_secret = res.group(6)
qr_issuer = res.group(8)

qr_identifiant = urllib.parse.quote(input("Identifiant [" + qr_identifiant + "] : ")) or qr_identifiant
qr_user = input("User [" + qr_user + "] : ") or qr_user
qr_issuer = urllib.parse.quote(input("Issuer [" + qr_issuer + "] : ")) or qr_issuer

new_qr = "otpauth://totp/" + qr_identifiant + ":" + qr_user  + "?secret=" + qr_secret + "&issuer=" + qr_issuer
print(new_qr)
img = qrcode.make(new_qr)
#img.show()
img.save("result.jpg")"""


# ==================================================================================
#
#   Gestion de l'application "console"
#
# ==================================================================================

# attention aux secrets qui restent (/tmp en RAM ?)

kb = KeyBindings()

@kb.add('c-c')
def _(event):
    event.app.exit()


#
# Elément "titre"
# 
init_text = "\n       ___  ____      ___        ______\n" + \
    "      / _ \|  _ \    / \ \      / / ___| \n" + \
    "     | | | | |_) |  / _ \ \ /\ / /\___ \ \n" + \
    "     | |_| |  _ <  / ___ \ V  V /  ___) | \n"+ \
    "      \__\_\_| \_\/_/   \_\_/\_/  |____/ \n\n" + \
    " Application de gestion des QRCodes pour AWS\n"

title = FormattedTextControl(text=init_text)
title_window = Window(
    content=title, 
    always_hide_cursor=True, 
    height=10, 
    width=160,
    align=WindowAlign.LEFT,
    )

#
# Elément affichage "choix utilisateur"
#
cmd_txt = FormattedTextControl(text="1) Lister les QR Codes\n2) Ajouter un QR Code (racine)\n3) Ajouter un QR Code (utilisateur)\n4) Sortir (4 ou CTRL+C)")
aff_window = Window(
    content=cmd_txt, 
    always_hide_cursor=True, 
    width=160,
    )

#
# Elément saisie du choix utilisateur
#
def cmd_handler(buff):
    #
    # On ne garde que le 1er caractère saisi, ça évite les injections dans ce programme hautement sensible
    #
    choix = int(buff.text[0])
    if choix == 1:
        list_txt = FormattedTextControl(text="1 sdgsdgsdgsdgsdg\n2 sgsgsdgsdgsdgsdg\n3 sdfsdfdsfsdfsdfsd\n4 sdsdsdgsgsgds")
        aff_window.content = list_txt
    elif choix == 2:
        pass
    elif choix == 3:
        pass
    elif choix == 4:
        get_app.exit() # marche pas
    get_app().reset()

cmd_input_field = TextArea(accept_handler = cmd_handler, height=1, prompt='>>> ', style='class:input-field', multiline=False, wrap_lines=False)
main_layout = Layout(HSplit([title_window, aff_window, cmd_input_field], width=162))

#
# Elément "liste des QR Codes"
#
list_txt = FormattedTextControl(text="1 sdgsdgsdgsdgsdg\n2 sgsgsdgsdgsdgsdg\n3 sdfsdfdsfsdfsdfsd\n4 sdsdsdgsgsgds")

#
# Lancement de l'application "console"
#
liste_qr = lecture_QR()
app = Application(layout=main_layout, key_bindings=kb, full_screen=True, erase_when_done=True)
app.run()
ecriture_QR(liste_qr)

#
#  EOF
#
print("Fin normale de l'application QRAWS")




