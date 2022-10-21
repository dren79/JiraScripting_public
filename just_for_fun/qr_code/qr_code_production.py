import os

import qrcode
from qrcode.image.styledpil import StyledPilImage
from qrcode.image.styles.moduledrawers import RoundedModuleDrawer
from qrcode.image.styles.colormasks import RadialGradiantColorMask


def make_qr_code(url):
    qr = qrcode.QRCode(version=1, box_size=5, border=5)
    qr.add_data(url)
    qr.make()

    img = qr.make_image(fill_color='black', back_color='white')
    return img


def make_qr_with_image_code(url, image):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(url)
    img = qr.make_image(image_factory=StyledPilImage, embeded_image_path=image)
    return img


def make_qr_with_colour_mask_code(url):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(url)
    img = qr.make_image(image_factory=StyledPilImage, color_mask=RadialGradiantColorMask())
    return img


def make_rounded_qr_code(url):
    qr = qrcode.QRCode(error_correction=qrcode.constants.ERROR_CORRECT_H)
    qr.add_data(url)
    img = qr.make_image(image_factory=StyledPilImage, module_drawer=RoundedModuleDrawer())
    return img


if __name__ == "__main__":
    website_link = 'https://www.devfestireland.com/'
    my_path = "qr_codes"
    image_path = "images/devfestireland.png"

    file_name = "devfestireland_standard.png"
    saved_path = os.path.join(my_path, file_name)
    qr_code = make_qr_code(website_link)
    qr_code.save(saved_path)

    file_name = "devfestireland_with_image.png"
    saved_path = os.path.join(my_path, file_name)
    qr_code = make_qr_with_image_code(website_link, image_path)
    qr_code.save(saved_path)

    file_name = "devfestireland_with_mask.png"
    saved_path = os.path.join(my_path, file_name)
    qr_code = make_qr_with_colour_mask_code(website_link)
    qr_code.save(saved_path)

    file_name = "devfestireland_rounded.png"
    saved_path = os.path.join(my_path, file_name)
    qr_code = make_rounded_qr_code(website_link)
    qr_code.save(saved_path)

