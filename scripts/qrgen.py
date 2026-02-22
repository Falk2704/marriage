import qrcode

qr = qrcode.QRCode(
    version=1,
    error_correction=qrcode.constants.ERROR_CORRECT_L,
    box_size=10,
    border=4,
)
qr.add_data("""BEGIN:VCALENDAR\r
VERSION:2.0\r
BEGIN:VEVENT\r
DTSTART;VALUE=DATE:20260829\r
DTEND;VALUE=DATE:20260830\r
SUMMARY:Hochzeit Isabell & Falk 👰🤵\r
LOCATION:Hotel Freihof Prichsenstadt, Freihofgasse 3, 97357 Prichsenstadt, Germany\r
IMAGE;VALUE=URI:https://example.com/images/hochzeit_banner.jpg\r\n\
X-APPLE-STRUCTURED-LOCATION;VALUE=URI;X-ADDRESS=Hotel Freihof Prichsenstadt\, Freihofgasse 3\, 97357 Prichsenstadt\, Germany;X-TITLE=Hotel Freihof Prichsenstadt\, Freihofgasse 3\, 97357 Prichsenstadt\, Germany;X-APPLE-RADIUS=141.175073:geo:49.817997,10.354053\r
END:VEVENT\r
END:VCALENDAR""")
qr.make(fit=True)

img = qr.make_image(fill_color="black", back_color=(244, 239, 229))
img.save("../assets/some_file.png")
