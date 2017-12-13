from pyzbar.pyzbar import decode
from PIL import Image
import webbrowser
import xlwings as xw
import pandas
import openpyxl

im = Image.open("QRtext1.png")
qr = str(decode(im))
print(qr)

qr = qr.replace("[Decoded(data=b'","")
qr = qr.replace("', type='QRCODE')]","")

print(qr)

webbrowser.open(qr)

wb = xw.Book()
sht = wb.sheets['Sheet1']
sht.range("A1").column_width = 18
sht.range("B1").column_width = 40

sht.range("A1").value = "Data #"
sht.range("B1").value = "Output"

sht.range("A2").value = pandas.to_datetime('now')
sht.range("B2").value = str(qr)
sht.range("B2").number_format = "###"


