from PySide6 import QtCore

from ventana import Ventana
# from tarea import tarea

class conectar_botones:
    def __init__(self):
        self.__ventana = Ventana()
        # self.__modelo = ventana.modelo_tareas


    def agregar_tarea(self):
        __ingreso_tarea = self.ui.ingreso_tarea.text()
        if __ingreso_tarea:
            texto = QStandardItem(__ingreso_tarea)
            self.modelo_tareas.appendRow(texto)
            self.ui.ingreso_tarea.clear()
        else:
            QMessageBox.warning(self, "Error", "El campo de texto está vacío")

    def completar_tarea(self):
        __tarea_vacia = self.ui.tableTareaVacia.currentIndex()
        __tarea_completada = self.ui.tableTareaCompletada.currentIndex()

        if __tarea_vacia.isValid():
            texto_tarea = self.modelo_tareas.itemFromIndex(__tarea_vacia).text()
            self.modelo_tareas_completadas.appendRow(QStandardItem(texto_tarea))
            self.modelo_tareas.removeRow(__tarea_vacia.row())
        elif __tarea_completada.isValid():
            QMessageBox.warning(self, "Error", "La tarea ya está completada.")
        else:
            QMessageBox.warning(self, "Error", "Primero selecciona la tarea.")

    def eliminar_tarea(self):
        __tarea_vacia = self.ui.tableTareaVacia.currentIndex()
        __tarea_completada = self.ui.tableTareaCompletada.currentIndex()

        if __tarea_vacia.isValid():
            self.modelo_tareas.removeRow(__tarea_vacia.row())
        elif __tarea_completada.isValid():
            self.modelo_tareas_completadas.removeRow(__tarea_completada.row())
        else:
            QMessageBox.warning(self, "Error", "Primero selecciona la tarea")

