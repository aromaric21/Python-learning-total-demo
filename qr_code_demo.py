import generate_qrc

img = qrcode.make("Hello World from Pybeginners !")
img.save("hello_qr.jpg")
img.show()

