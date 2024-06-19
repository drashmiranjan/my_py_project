# here me make a Qr code for my linkedin
import qrcode as qr

link_qr_img = qr.make("https://www.linkedin.com/in/rashmi-ranjan-das-89b914245/")

link_qr_img.save("my_linkedin_qr.png")