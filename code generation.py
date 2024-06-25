import qrcode

features=qrcode.QRCode(version=1,box_size=40,border=3)

features.add_data('https://www.instagram.com/atmanand_inamati/visitmyprofile')
features.make(fit=True)

generate_image= features.make_image(fill_color='blue', back_color='white')
generate_image.save("qrcode2.png")
import qrcode

features=qrcode.QRCode(version=1,box_size=40,border=3)

features.add_data('https://www.instagram.com/atmanand_inamati/visitmyprofile')
features.make(fit=True)

generate_image= features.make_image(fill_color='blue', back_color='white')
generate_image.save("qrcode2.png")