from PySide6 import QtCore
from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QMessageBox
from ventana import Ventana

class ConectarBotones:
    def __init__(self, ventana):
        self.__ventana = ventana
        self.__modelo_tareas = self.__ventana.ui.modelo_tareas
        self.__modelo_tareas_completadas = self.__ventana.ui.modelo_tareas_completadas

    def agregar_tarea(self):
        ingreso_tarea = self.__ventana.ui.ingreso_tarea.text()
        if ingreso_tarea:
            texto = QStandardItem(ingreso_tarea)
            self.__modelo_tareas.appendRow(texto)
            self.__ventana.ui.ingreso_tarea.clear()
        else:
            QMessageBox.warning(self.__ventana, "Error", "El campo de texto está vacío")

    def completar_tarea(self):
        tarea_vacia = self.__ventana.ui.tableTareaVacia.currentIndex()
        tarea_completada = self.__ventana.ui.tableTareaCompletada.currentIndex()

        if tarea_vacia.isValid():
            texto_tarea = self.__modelo_tareas.itemFromIndex(tarea_vacia).text()
            self.__modelo_tareas_completadas.appendRow(QStandardItem(texto_tarea))
            self.__modelo_tareas.removeRow(tarea_vacia.row())
        elif tarea_completada.isValid():
            QMessageBox.warning(self.__ventana, "Error", "La tarea ya está completada.")
        else:
            QMessageBox.warning(self.__ventana, "Error", "Primero selecciona la tarea.")

    def eliminar_tarea(self):
        tarea_vacia = self.__ventana.ui.tableTareaVacia.currentIndex()
        tarea_completada = self.__ventana.ui.tableTareaCompletada.currentIndex()

        if tarea_vacia.isValid():
            self.__modelo_tareas.removeRow(tarea_vacia.row())
        elif tarea_completada.isValid():
            self.__modelo_tareas_completadas.removeRow(tarea_completada.row())
        else:
            QMessageBox.warning(self.__ventana, "Error", "Primero selecciona la tarea")
