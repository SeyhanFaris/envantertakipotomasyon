import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import *
from EkiplerPenceresi1_0 import *
import sqlite3 as sql


uygulama = QApplication(sys.argv)
pencere = QMainWindow()
ui = Ui_MainWindow()
ui.setupUi(pencere)
pencere.show()

#veritabanı işlemleri
baglanti = sql.connect("seyhanEkiplerdb.sqlite")
islem = baglanti.cursor()
baglanti.commit()

table = islem.execute("create table if not exists urun(sahaId text, isTipi text, personel text, aciklama text)")
baglanti.commit()

def kayit_ekle():
    SahaId = ui.textEdit.toPlainText()
    IsTipi = ui.textEdit_2.toPlainText()
    Personel = ui.textEdit_3.toPlainText()
    Aciklama = ui.textEdit_4.toPlainText()

    try:
        ekle = "insert into urun (sahaId, isTipi, personel, aciklama) values (?,?,?,?)"
        islem.execute(ekle,(SahaId,IsTipi,Personel,Aciklama))       
        baglanti.commit()
        ui.statusbar.showMessage("Kayıt Ekleme Başarılı",1)
    except Exception as error:
        ui.statusbar.showMessage("Kayıt Eklenemedi Hata !"+str(error))

def kayit_listele():
    ui.tableWidget.clear()
    ui.tableWidget.setHorizontalHeaderLabels(("Saha ID","İş Tipi","Personel","Açıklama"))

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

ui.btn1.clicked.connect(kayit_ekle)
ui.btn3.clicked.connect(kayit_sil)
ui.btn2.clicked.connect(kayit_guncelle)

#sys.exit(uygulama.exec_())