import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
from PyQt5.QtWidgets import *
from LoginPanel import *
import sqlite3 as sql

uygulama = QApplication(sys.argv)
pencere = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(pencere)
pencere.show()

kullanicilar = []
sifreler = []

vt = sql.connect("hesaplar.sqlite")
im = vt.cursor()
vt.commit()
sorgu = im.execute("select kullanici from hesaplar")
veri = im.fetchall()
for i in veri:
    for x in i:
        kullanicilar.append(x)

sorgu2 = im.execute("select sifre from hesaplar")
veri2 = im.fetchall()
for a in veri2:
    for b in a:
        sifreler.append(b)

def girisYap():
    kullaniciAdi = ui.textbox1.text()
    sifre = ui.textbox2.text()

    if kullaniciAdi in kullanicilar and sifre in sifreler:
        from main import pencere
    
def kayitOl():
    kullaniciAdi = ui.textbox1.text()
    sifre = ui.textbox2.text()
    ekleme = im.execute("insert into hesaplar(kullanici,sifre) values(?,?)",(kullaniciAdi,sifre))
    vt.commit()

 
    
ui.grsBtn.clicked.connect(girisYap)
ui.kytBtn.clicked.connect(kayitOl)

sys.exit(uygulama.exec_())
vt.close()