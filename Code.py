import qrcode
qr=qrcode.QRCode(    #define the structure and size of that Qr code structure.
    version=2,
    box_size=10,
    border=6
)
 
data="https://www.linkedin.com/in/parth-madan-51a1b5192"   #In data we have to provide link of what we have to acess thhroug Qrcode
qr.add_data(data)
qr.make(fit=True)
img=qr.make_image(fill="black",back_color="white")
img.save("Qrpic.png")  #img.save refers
