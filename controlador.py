from PySide6.QtGui import QStandardItem, QStandardItemModel
from PySide6.QtWidgets import QMessageBox
from tarea import Tarea


class ConectarBotones:
    def __init__(self, ventana):
        self.__modelo_tareas_vacias = QStandardItemModel()
        self.__modelo_tareas_completadas = QStandardItemModel()
        self.__ventana = ventana
        self.__ventana.tableTareaVacia.setModel(self.__modelo_tareas_vacias)  # Acceder a la tabla vacia (izq)
        self.__ventana.tableTareaCompletada.setModel(self.__modelo_tareas_completadas)  # Acceder a tabla vacia (derec)


    def agregar_tarea(self):
        ingreso_tarea = self.__ventana.ingreso_tarea.text()
        if ingreso_tarea:
            tarea = Tarea(ingreso_tarea)
            self.__modelo_tareas_vacias.appendRow(QStandardItem(str(tarea)))
            self.__ventana.ingreso_tarea.clear()
        else:
            QMessageBox.warning(self.__ventana, "Error", "El campo de texto está vacío")


    def completar_tarea(self):
        tarea_vacia = self.__ventana.tableTareaVacia.currentIndex()
        tarea_completada = self.__ventana.tableTareaCompletada.currentIndex()

        if tarea_vacia.isValid():
            texto_tarea = self.__modelo_tareas_vacias.itemFromIndex(tarea_vacia).text()
            self.__modelo_tareas_completadas.appendRow(QStandardItem(texto_tarea))
            self.__modelo_tareas_vacias.removeRow(tarea_vacia.row())
        elif tarea_completada.isValid():
            QMessageBox.warning(self.__ventana, "Error", "La tarea ya está completada.")
        else:
            QMessageBox.warning(self.__ventana, "Error", "Primero selecciona la tarea.")


    def eliminar_tarea(self):
        tarea_vacia = self.__ventana.tableTareaVacia.currentIndex()
        tarea_completada = self.__ventana.tableTareaCompletada.currentIndex()

        if tarea_vacia.isValid():
            self.__modelo_tareas_vacias.removeRow(tarea_vacia.row())
        elif tarea_completada.isValid():
            self.__modelo_tareas_completadas.removeRow(tarea_completada.row())
        else:
            QMessageBox.warning(self.__ventana, "Error", "Primero selecciona la tarea.")