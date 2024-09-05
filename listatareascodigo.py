from PySide6.QtWidgets import QApplication, QWidget, QMessageBox, QVBoxLayout
from PySide6.QtGui import QStandardItemModel, QStandardItem
from ListaTareas import Ui_Form


class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Lista de Tareas")

        self.layout = QVBoxLayout(self)
        self.setLayout(self.layout)

        self.ui.tableTareaVacia.horizontalHeader().setVisible(False)
        self.ui.tableTareaVacia.verticalHeader().setVisible(False)
        self.ui.tableTareaCompletada.horizontalHeader().setVisible(False)
        self.ui.tableTareaCompletada.verticalHeader().setVisible(False)

        self.ui.tableTareaVacia.horizontalHeader().setStretchLastSection(True)
        self.ui.tableTareaCompletada.horizontalHeader().setStretchLastSection(True)


class Tarea(Ventana):
    def __init__(self):
        super().__init__()
        self.conectar_botones()

        self.modelo_tareas = QStandardItemModel(self)
        self.modelo_tareas_completadas = QStandardItemModel(self)
        self.ui.tableTareaVacia.setModel(self.modelo_tareas)
        self.ui.tableTareaCompletada.setModel(self.modelo_tareas_completadas)

    def conectar_botones(self):
        self.ui.boton_agregar_tarea.clicked.connect(self.agregar_tarea)
        self.ui.boton_eliminar_tarea.clicked.connect(self.eliminar_tarea)
        self.ui.boton_completar_tarea.clicked.connect(self.completar_tarea)

    def agregar_tarea(self):
        ingreso_tarea = self.ui.ingreso_tarea.text()
        if ingreso_tarea:
            texto = QStandardItem(ingreso_tarea)
            self.modelo_tareas.appendRow(texto)
            self.ui.ingreso_tarea.clear()
        else:
            QMessageBox.warning(self, "Error", "El campo de texto está vacío")

    def completar_tarea(self):
        tarea_vacia = self.ui.tableTareaVacia.currentIndex()
        tarea_completada = self.ui.tableTareaCompletada.currentIndex()

        if tarea_vacia.isValid():
            texto_tarea = self.modelo_tareas.itemFromIndex(tarea_vacia).text()
            self.modelo_tareas_completadas.appendRow(QStandardItem(texto_tarea))
            self.modelo_tareas.removeRow(tarea_vacia.row())
        elif tarea_completada.isValid():
            QMessageBox.warning(self, "Error", "La tarea ya está completada.")
        else:
            QMessageBox.warning(self, "Error", "Primero selecciona la tarea.")

    def eliminar_tarea(self):
        tarea_vacia = self.ui.tableTareaVacia.currentIndex()
        tarea_completada = self.ui.tableTareaCompletada.currentIndex()

        if tarea_vacia.isValid():
            self.modelo_tareas.removeRow(tarea_vacia.row())
        elif tarea_completada.isValid():
            self.modelo_tareas_completadas.removeRow(tarea_completada.row())
        else:
            QMessageBox.warning(self, "Error", "Primero selecciona la tarea.")


if __name__ == "__main__":
    app = QApplication([])
    tarea = Tarea()
    tarea.show()
    app.exec()
