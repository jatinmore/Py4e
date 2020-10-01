from pyqrcode import QRCode


qr=pyqrcode.QRcode(version=1,bor_size=10,border=4)
qr.add_data('text')
qr.make()
img=qr.make_image(fill_color="red",back_color="white")
img.save('test.png')

