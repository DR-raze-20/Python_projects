import qrcode
url=input('Enter The url:').strip()
file_path='F:\\PYTHON_MALWARE_PRAC\\qrcode.png'
qr=qrcode.QRCode()
qr.add_data(url)
img = qr.make_image()
img.save(file_path)
print('Qr-generated')
