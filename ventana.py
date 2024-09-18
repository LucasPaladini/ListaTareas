from PySide6 import QtCore
from PySide6.QtWidgets import QWidget, QMessageBox
from PySide6.QtGui import QStandardItemModel
from listatareas import Ui_Form
from controlador import ConectarBotones

class Ventana(QWidget):

    def __init__(self):
        super().__init__()
        self.__ui = Ui_Form()
        self.__ui.setupUi(self)
        self.setWindowTitle("Lista de Tareas")
        self.__conectar_botones = ConectarBotones(self)

        self.__ui.boton_agregar_tarea.clicked.connect(self.__conectar_botones.agregar_tarea)
        self.__ui.boton_eliminar_tarea.clicked.connect(self.__conectar_botones.eliminar_tarea)
        self.__ui.boton_completar_tarea.clicked.connect(self.__conectar_botones.completar_tarea)

        # self.__modelo_tareas = QStandardItemModel(self)
        # self.__modelo_tareas_completadas = QStandardItemModel(self)
        # self.__ui.tableTareaVacia.setModel(self.__modelo_tareas)
        # self.__ui.tableTareaCompletada.setModel(self.__modelo_tareas_completadas)

        self.__ui.tableTareaVacia.horizontalHeader().setVisible(False)
        self.__ui.tableTareaVacia.verticalHeader().setVisible(False)
        self.__ui.tableTareaCompletada.horizontalHeader().setVisible(False)
        self.__ui.tableTareaCompletada.verticalHeader().setVisible(False)

        self.__ui.tableTareaVacia.horizontalHeader().setStretchLastSection(True)
        self.__ui.tableTareaCompletada.horizontalHeader().setStretchLastSection(True)
