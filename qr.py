import re
import qrcode
import pprint
from pyzbar.pyzbar import decode
from PIL import Image

inputImage = Image.open("test.jpg")
infos = decode(inputImage)
b_txt = infos[0][0].replace(b'\n',b'')
txt = b_txt.decode()

regle = r"(otpauth\:\/\/totp\/)(\w+)(\?secret\=)([A-Z0-9]{64})(&issuer=)([\w+])"
regle = r"(otpauth:\/\/totp\/)(.+)(:)(.+)(\?secret=)([A-Z0-9]{64})(\&issuer\=)(.+)"
res = re.match(regle, txt)

new_qr = "otpauth://totp/" + "nom_du_compte" + ":" + res.group(4) + "?secret=" + res.group(6) + "&issuer=" + "SG-SRO"
img = qrcode.make(new_qr)
img.show()
