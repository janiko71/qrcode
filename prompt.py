from prompt_toolkit import Application, prompt
from prompt_toolkit.buffer import Buffer
from prompt_toolkit.enums import DEFAULT_BUFFER
from prompt_toolkit.layout.layout import Layout
from prompt_toolkit.layout import NumberedMargin, ScrollOffsets, WindowAlign
from prompt_toolkit.layout.containers import Window, FloatContainer, Float, HSplit, VSplit
from prompt_toolkit.layout.controls import BufferControl, FormattedTextControl

from prompt_toolkit.layout.screen import Screen
from prompt_toolkit.layout.dimension import D
from prompt_toolkit.styles import Style

from prompt_toolkit.application import get_app

from prompt_toolkit.key_binding import KeyBindings
from prompt_toolkit import print_formatted_text, HTML
from prompt_toolkit.widgets import Frame, Box, Button, TextArea, RadioList
#from prompt_toolkit.layout.containers import VSplit, Window
from prompt_toolkit.shortcuts import yes_no_dialog, PromptSession
#from prompt_toolkit import PromptSession

import pprint

# attention aux secrets qui restent (/tmp en RAM ?)

kb = KeyBindings()

@kb.add('c-c')
def _(event):
    event.app.exit()


init_text = "\n       ___  ____      ___        ______\n" + \
    "      / _ \|  _ \    / \ \      / / ___| \n" + \
    "     | | | | |_) |  / _ \ \ /\ / /\___ \ \n" + \
    "     | |_| |  _ <  / ___ \ V  V /  ___) | \n"+ \
    "      \__\_\_| \_\/_/   \_\_/\_/  |____/ \n\n" + \
    " Application de gestion des QRCodes pour AWS\n"
#window = Layout(Window(content=FormattedTextControl(text="Ceci est mon texte\nCeci est mon contrôle\nCeci est rien du tout"), always_hide_cursor=True, left_margins=[NumberedMargin()]))
title = FormattedTextControl(text=init_text)
title_window = Window(
    content=title, 
    always_hide_cursor=True, 
    height=10, 
    width=160,
    align=WindowAlign.LEFT,
    )

cmd = FormattedTextControl(text="1) Lister les QR Codes\n2) Ajouter un QR Code (racine)\n3) Ajouter un QR Code (utilisateur)\n4) Sortir (4 ou CTRL+C)")
cmd_window = Window(
    content=cmd, 
    always_hide_cursor=True, 
    width=160,
    )

#buf = Buffer(name='cmd_entry', multiline=False, accept_handler=cmd_handler())

def cmd_handler(buff):
    print(buff.text)
    # On ne garde que le 1er caractère saisi, ça évite les injections dans ce programme hautement sensible
    choix = int(buff.text[0])
    if choix == 1:
        pass
    elif choix == 2:
        pass
    elif choix == 3:
        pass
    elif choix == 4:
        get_app.exit() # marche pas
    get_app().reset()

cmd_input_field = TextArea(accept_handler = cmd_handler, height=1, prompt='>>> ', style='class:input-field', multiline=False, wrap_lines=False)
main_layout = Layout(HSplit([title_window, cmd_window, cmd_input_field], width=162))

# Layout liste des QR Code
list_txt = FormattedTextControl(text="1 sdgsdgsdgsdgsdg\n2 sgsgsdgsdgsdgsdg\n3 sdfsdfdsfsdfsdfsd\n4 sdsdsdgsgsgds")
list_window = Window(
    content=list_txt, 
    always_hide_cursor=True, 
    height=10, 
    width=160,
    align=WindowAlign.LEFT,
    )
list_layout = Layout(HSplit([title_window, list_window], width=162))


app = Application(layout=main_layout, key_bindings=kb, full_screen=True, erase_when_done=True)
# ajouter Input instance (écoute des touches)

"""s = PromptSession(message='Votre choix > ')
text = s.prompt()"""

app.run()

#b.print_formatted_text(HTML('<skyblue>This is <b>sky</b> blue</skyblue>'))
print("Fin de l'application QRAWS")

