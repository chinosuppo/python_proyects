
import qrcode

link = "https://www.linkedin.com/in/carlos-suppo/"

img = qrcode.make(link)

img.save("C:/Users/Chino/Desktop/proyects/codificador_QR/myqrcode.png")

qr = qrcode.QRCode(version = 1, box_size=20, border=10)
qr.add_data(link)

qr.make(fit=True)

img = qr.make_image(fill_color = 'blue', back_color = 'green') # no me genera el cambio de color en el nuevo qr

img.save("C:/Users/Chino/Desktop/proyects/codificador_QR/myqrcode1.png")

### No pude realizar la parte de decodificación porque no dejaba instalar paquete PIL ###