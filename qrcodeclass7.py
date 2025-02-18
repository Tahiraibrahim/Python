import qrcode
img = qrcode.make("https://www.linkedin.com/in/tahira-ibrahim-g-18761b26b/")
print(type(img))
img.save("tahiralinkedin.png")
print('QR code has been generated sucessfully')