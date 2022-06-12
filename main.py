import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from AnaEkran1_0 import *
import sqlite3 as sql
import cv2
import time
from pyzbar.pyzbar import decode


uygulama = QApplication(sys.argv)
pencere = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(pencere)
pencere.show()


def actionEkipler_selected():
    from main2 import pencere
    pencere.show()

ui.actionEkipler.triggered.connect(actionEkipler_selected)

#veritabanı işlemleri
baglanti = sql.connect("seyhandb.sqlite")
islem = baglanti.cursor()
baglanti.commit()

table = islem.execute("create table if not exists urun(sahaId text, isTipi text, personel text, aciklama text, barkodNo int)")
baglanti.commit()

def barkod_oku():
    global barcodes
    cap = cv2.VideoCapture(0)
    cap.set(3, 640) # width
    cap.set(4, 480) # height
    valid_codes = []
    used_codes = []

    camera = True
    while camera == True:
        success, Frame = cap.read()

        for code in decode(Frame):
            if code.data.decode('utf-8') not in used_codes:
                print('Kod okundu!.'"Giriş yapıldı")
                #kod bu
                barcodes = code.data.decode("utf-8")
                print(barcodes)
                used_codes.append(code.data.decode('utf-8'))
                time.sleep(2)
            else:
                pass

        cv2.imshow("testing-code-scan", Frame)
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

def kayit_ekle():
    SahaId = ui.textEdit.toPlainText()
    IsTipi = ui.textEdit_2.toPlainText()
    Personel = ui.textEdit_3.toPlainText()
    Aciklama = ui.textEdit_4.toPlainText()
    Barkod = barcodes
    
    if Barkod == "":
        Barkod = 0

    try:
        ekle = "insert into urun (sahaId, isTipi, personel, aciklama, barkodNo) values (?,?,?,?,?)"
        islem.execute(ekle,(SahaId,IsTipi,Personel,Aciklama,Barkod))       
        baglanti.commit()
        ui.statusbar.showMessage("Kayıt Ekleme Başarılı",1)
    except Exception as error:
        ui.statusbar.showMessage("Kayıt Eklenemedi Hata !"+str(error))

def kayit_listele():
    ui.tableWidget.clear()
    ui.tableWidget.setHorizontalHeaderLabels(("Saha ID","İş Tipi","Personel","Açıklama","Barkod No"))

    sorgu = "select * from urun"
    islem.execute(sorgu)
    print(islem.execute(sorgu))

    for indexSatir, kayitNumarasi in enumerate(islem):
        for indexSutun, kayitSutun in enumerate(kayitNumarasi):
            ui.tableWidget.setItem(indexSatir,indexSutun,QTableWidgetItem(str(kayitSutun)))

def kayit_sil():
    secilen_kayit = ui.tableWidget.selectedItems()
    silinecek_kayit = secilen_kayit[0].text()

    sorgu = "delete from urun where sahaId = ?"

    try:
        islem.execute(sorgu,(silinecek_kayit,))
        baglanti.commit()
        ui.statusbar.showMessage("Kayıt Başarıyla Silindi")
    except Exception as error:
        ui.statusbar.showMessage("Kayıt Silinirken Bir Hata oluştu "+str(error))


def kayit_guncelle():
    SahaId = ui.textEdit.toPlainText()
    IsTipi = ui.textEdit_2.toPlainText()
    Personel = ui.textEdit_3.toPlainText()
    Aciklama = ui.textEdit_4.toPlainText()

    if SahaId == "" and IsTipi == "" and Personel == "" and Aciklama == "":
        islem.execute("update urun set personel = ? where sahaId = ?",(SahaId,Personel))
    else:
        islem.execute("update urun set aciklama = ?, isTipi = ?, personel = ? where sahaId = ?",(Aciklama,IsTipi,Personel,SahaId))
    baglanti.commit()
    kayit_listele()

ui.pushButton.clicked.connect(kayit_ekle)
ui.pushButton_4.clicked.connect(kayit_listele)
ui.pushButton_3.clicked.connect(kayit_sil)
ui.pushButton_5.clicked.connect(barkod_oku)
ui.pushButton_2.clicked.connect(kayit_guncelle)

#sys.exit(uygulama.exec_())