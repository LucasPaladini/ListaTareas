# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'ui.ui'
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
        Form.resize(474, 337)
        Form.setStyleSheet(u"background-color: rgb(199, 199, 199)")
        self.gridLayout = QGridLayout(Form)
        self.gridLayout.setObjectName(u"gridLayout")
        self.ingreso_tarea = QLineEdit(Form)
        self.ingreso_tarea.setObjectName(u"ingreso_tarea")
        self.ingreso_tarea.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout.addWidget(self.ingreso_tarea, 0, 0, 1, 2)

        self.boton_agregar_tarea = QPushButton(Form)
        self.boton_agregar_tarea.setObjectName(u"boton_agregar_tarea")
        self.boton_agregar_tarea.setAutoDefault(False)
        self.boton_agregar_tarea.setFlat(False)

        self.gridLayout.addWidget(self.boton_agregar_tarea, 0, 2, 1, 1)

        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.labelTarea = QLabel(Form)
        self.labelTarea.setObjectName(u"labelTarea")

        self.gridLayout_4.addWidget(self.labelTarea, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.tableTareaVacia = QTableView(Form)
        self.tableTareaVacia.setObjectName(u"tableTareaVacia")

        self.gridLayout_4.addWidget(self.tableTareaVacia, 1, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_4, 1, 0, 1, 1)

        self.gridLayout_5 = QGridLayout()
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.labelTareasCompletadas = QLabel(Form)
        self.labelTareasCompletadas.setObjectName(u"labelTareasCompletadas")

        self.gridLayout_5.addWidget(self.labelTareasCompletadas, 0, 0, 1, 1, Qt.AlignmentFlag.AlignHCenter)

        self.tableTareaCompletada = QTableView(Form)
        self.tableTareaCompletada.setObjectName(u"tableTareaCompletada")
        font = QFont()
        font.setStrikeOut(True)
        self.tableTareaCompletada.setFont(font)

        self.gridLayout_5.addWidget(self.tableTareaCompletada, 1, 0, 1, 1)


        self.gridLayout.addLayout(self.gridLayout_5, 1, 1, 1, 2)

        self.boton_completar_tarea = QPushButton(Form)
        self.boton_completar_tarea.setObjectName(u"boton_completar_tarea")

        self.gridLayout.addWidget(self.boton_completar_tarea, 2, 0, 1, 1)

        self.boton_eliminar_tarea = QPushButton(Form)
        self.boton_eliminar_tarea.setObjectName(u"boton_eliminar_tarea")

        self.gridLayout.addWidget(self.boton_eliminar_tarea, 2, 2, 1, 1)


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
        self.labelTarea.setText(QCoreApplication.translate("Form", u"Tareas", None))
        self.labelTareasCompletadas.setText(QCoreApplication.translate("Form", u"Tareas completadas", None))
        self.boton_completar_tarea.setText(QCoreApplication.translate("Form", u"Marcar como completada", None))
        self.boton_eliminar_tarea.setText(QCoreApplication.translate("Form", u"Eliminar", None))
    # retranslateUi

