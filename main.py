from time import strftime
from PyQt5.QtGui import QIcon,QColor,QFont
from PyQt5.QtWidgets import  QFileDialog, QInputDialog, QMainWindow, QWidget, QMessageBox,QDialog,QTableWidgetItem 
from PyQt5.QtCore import QCoreApplication,QTimer,QElapsedTimer, Qt
from PyQt5 import QtWidgets, uic
from datetime import datetime as dt
import sys,sqlite3,os,pickle ,datetime, json
from registro import Registro



class Login(QMainWindow):
    def __init__(self):
        QMainWindow.__init__(self)
        uic.loadUi('login.ui', self)
        self.setWindowTitle('Login al Sistema')
        self.setWindowIcon(QIcon('icon.png'))
        self.Registrar.clicked.connect(self.registro)
        self.LOGin.clicked.connect(self.logIN)
        self.LOGout.clicked.connect(self.logOUT)
    def logIN(self):
        if self.Usuario.text() != "" and self.Contra.text() != "":
            try:
                b = False
                with open("Usuarios.json","r")as usuarios:
                    usuariostotales = json.load(usuarios)
                    for user in usuariostotales["Usuarios"]:
                        if self.Usuario.text() == user[0] and self.Contra.text() == user[1]:
                            self.usr.setText(user[0])
                            self.nom.setText(user[2])
                            self.ape.setText(user[3])
                            self.LOGout.setEnabled(True)
                            self.LOGin.setEnabled(False)
                            b = True
                            QMessageBox.information(self,"Login","Login Exitoso")
                            return b
                if b == False:
                    QMessageBox.information(self,"Login","Usuario o contraseña incorrecta")
            except Exception as e:
                QMessageBox.information(self,"Error","Error en el login")
    def logOUT(self):
        self.usr.setText("")
        self.nom.setText("")
        self.ape.setText("")
        self.LOGout.setEnabled(False)
        self.LOGin.setEnabled(True)
        self.Usuario.setText("")
        self.Contra.setText("")
    def registro(self):
        registro = Registro()
        registro.exec_()
    
if __name__ == "__main__":
    app = QtWidgets.QApplication(sys.argv)
    ventana = Login()
    ventana.show()
    sys.exit(app.exec_())