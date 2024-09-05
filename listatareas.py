# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ListaTarea_ui_2.ui'
##
## Created by: Qt User Interface Compiler version 6.7.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGridLayout, QHeaderView, QLabel,
    QLineEdit, QPushButton, QSizePolicy, QTableView,
    QWidget)

class Ui_Form(object):
    def setupUi(self, Form):
        if not Form.objectName():
            Form.setObjectName(u"Form")
        Form.resize(453, 326)
        Form.setStyleSheet(u"background-color: rgb(199, 199, 199)")
        self.ingreso_tarea = QLineEdit(Form)
        self.ingreso_tarea.setObjectName(u"ingreso_tarea")
        self.ingreso_tarea.setGeometry(QRect(20, 10, 321, 22))
        self.ingreso_tarea.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.boton_agregar_tarea = QPushButton(Form)
        self.boton_agregar_tarea.setObjectName(u"boton_agregar_tarea")
        self.boton_agregar_tarea.setGeometry(QRect(350, 10, 79, 21))
        self.boton_agregar_tarea.setAutoDefault(False)
        self.boton_agregar_tarea.setFlat(False)
        self.boton_eliminar_tarea = QPushButton(Form)
        self.boton_eliminar_tarea.setObjectName(u"boton_eliminar_tarea")
        self.boton_eliminar_tarea.setGeometry(QRect(350, 290, 81, 24))
        self.boton_completar_tarea = QPushButton(Form)
        self.boton_completar_tarea.setObjectName(u"boton_completar_tarea")
        self.boton_completar_tarea.setGeometry(QRect(20, 290, 151, 24))
        self.gridLayoutWidget = QWidget(Form)
        self.gridLayoutWidget.setObjectName(u"gridLayoutWidget")
        self.gridLayoutWidget.setGeometry(QRect(20, 49, 201, 231))
        self.gridLayout_4 = QGridLayout(self.gridLayoutWidget)
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.labelTarea = QLabel(self.gridLayoutWidget)
        self.labelTarea.setObjectName(u"labelTarea")

        self.gridLayout_4.addWidget(self.labelTarea, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.tableTareaVacia = QTableView(self.gridLayoutWidget)
        self.tableTareaVacia.setObjectName(u"tableTareaVacia")

        self.gridLayout_4.addWidget(self.tableTareaVacia, 1, 0, 1, 1)

        self.gridLayoutWidget_2 = QWidget(Form)
        self.gridLayoutWidget_2.setObjectName(u"gridLayoutWidget_2")
        self.gridLayoutWidget_2.setGeometry(QRect(230, 50, 201, 231))
        self.gridLayout_5 = QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.labelTareasCompletadas = QLabel(self.gridLayoutWidget_2)
        self.labelTareasCompletadas.setObjectName(u"labelTareasCompletadas")

        self.gridLayout_5.addWidget(self.labelTareasCompletadas, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.tableTareaCompletada = QTableView(self.gridLayoutWidget_2)
        self.tableTareaCompletada.setObjectName(u"tableTareaCompletada")
        font = QFont()
        font.setStrikeOut(True)
        self.tableTareaCompletada.setFont(font)

        self.gridLayout_5.addWidget(self.tableTareaCompletada, 1, 0, 1, 1)


        self.retranslateUi(Form)
        self.boton_eliminar_tarea.clicked.connect(self.tableTareaVacia.clearSelection)

        self.boton_agregar_tarea.setDefault(False)


        QMetaObject.connectSlotsByName(Form)
    # setupUi

    def retranslateUi(self, Form):
        Form.setWindowTitle(QCoreApplication.translate("Form", u"Form", None))
#if QT_CONFIG(tooltip)
        Form.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><br/></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
#if QT_CONFIG(tooltip)
        self.ingreso_tarea.setToolTip(QCoreApplication.translate("Form", u"<html><head/><body><p align=\"center\"><span style=\" font-weight:700;\"><br/></span></p></body></html>", None))
#endif // QT_CONFIG(tooltip)
        self.ingreso_tarea.setPlaceholderText(QCoreApplication.translate("Form", u"Agregar nueva tarea", None))
        self.boton_agregar_tarea.setText(QCoreApplication.translate("Form", u"Agregar tarea", None))
        self.boton_eliminar_tarea.setText(QCoreApplication.translate("Form", u"Eliminar", None))
        self.boton_completar_tarea.setText(QCoreApplication.translate("Form", u"Marcar como completada", None))
        self.labelTarea.setText(QCoreApplication.translate("Form", u"Tareas", None))
        self.labelTareasCompletadas.setText(QCoreApplication.translate("Form", u"Tareas completadas", None))
    # retranslateUi

