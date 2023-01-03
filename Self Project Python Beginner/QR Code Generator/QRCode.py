# install all the libraries needed
# create a function that collects a text and converts it to a qrcode
# save the qrcode as a image
# run the function

import qrcode

def generate_qrcode(text):

    qr = qrcode.QRCode(
        version = 1,
        error_correction = qrcode.constants.ERROR_CORRECT_L,
        box_size=15,
        border=5,
    )

    qr.add_data(text)
    qr.make(fit=True)
    img = qr.make_image(fill_colors="black", back_colors="while")
    img.save("qrimg0001.png")

url = input("Enter your url: ")
generate_qrcode(url)