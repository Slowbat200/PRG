# Import qrcode and BytesIO library
import qrcode
from io import BytesIO

# Create width and height for QR code
qr = qrcode.QRCode(
    error_correction=qrcode.constants.ERROR_CORRECT_H,
    box_size=10,
    border=4,
)

# Text which we want to make as QR
text = "Hello world"

# Create QR code
qr.add_data(text)
qr.make(fit=True)

# Color option for QR 
img = qr.make_image(fill_color="black", back_color="white")

# Save the image to a file
with open('qr_code.png', 'wb') as f:
    img.save(f)

# Save the image to a stream
buf = BytesIO()
img.save(buf, format='PNG')
image_data = buf.getvalue()
