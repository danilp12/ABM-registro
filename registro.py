from time import strftime
from PyQt5.QtGui import QIcon,QColor,QFont
from PyQt5.QtWidgets import  QFileDialog, QInputDialog, QMainWindow, QWidget, QMessageBox,QDialog,QTableWidgetItem 
from PyQt5.QtCore import QCoreApplication,QTimer,QElapsedTimer, Qt
from PyQt5 import QtWidgets, uic
from datetime import datetime as dt
import sys,sqlite3,os,pickle ,datetime, json




class Registro(QDialog):
    def __init__(self):
        QDialog.__init__(self)
        uic.loadUi('registro.ui', self)
        self.setWindowTitle('Registro al Sistema')
        self.setWindowIcon(QIcon('icon.png'))
        self.Registrar.clicked.connect(self.registrar)
        self.Cancelar.clicked.connect(self.close)
    def registrar(self):
        if self.User.text() != "" and self.Nombre.text() != "" and self.Apellido.text() != "":
            usuario = self.User.text()
            nombre = self.Nombre.text()
            apellido = self.Apellido.text()
            pasw = self.Passw.text()
            with open ( "Usuarios.json","r")as usuarios:
                usuariostotales = json.load(usuarios)
                usuariostotales["Usuarios"].append([usuario,pasw,nombre,apellido])
                with open ("Usuarios.json","w") as users:
                    json.dump(usuariostotales,users)
                    QMessageBox.information(self,"Guardado","Registro Completo")
                    
            self.close()
        else:
            QMessageBox.information(self,"Error","No Pueden quedar campos vacios en el registro")
        
