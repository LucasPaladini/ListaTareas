from PySide6.QtWidgets import QApplication, QWidget, QLineEdit, QMessageBox, QPushButton, QTableView, QVBoxLayout
from PySide6.QtGui import QStandardItemModel, QStandardItem
from ListaTareas import Ui_Form


class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        self.ui = Ui_Form()
        self.ui.setupUi(self)
        self.setWindowTitle("Lista de Tareas")
        self.layout = QVBoxLayout(self)
        self.conectar_botones()

        self.modelo_tareas = QStandardItemModel(self)
        self.modelo_tareas_completadas = QStandardItemModel(self)
        self.ui.tableTareaVacia.setModel(self.modelo_tareas)
        self.ui.tableTareaCompletada.setModel(self.modelo_tareas_completadas)

        self.ui.tableTareaVacia.horizontalHeader().setVisible(False)
        self.ui.tableTareaVacia.verticalHeader().setVisible(False)
        self.ui.tableTareaCompletada.horizontalHeader().setVisible(False)
        self.ui.tableTareaCompletada.verticalHeader().setVisible(False)

        self.header_tareas = self.ui.tableTareaVacia.horizontalHeader()
        self.header_completadas = self.ui.tableTareaCompletada.horizontalHeader()
        self.header_tareas.setStretchLastSection(True)
        self.header_completadas.setStretchLastSection(True)

    def conectar_botones(self):
        self.ui.boton_agregar_tarea.clicked.connect(self.agregar_tarea)
        self.ui.boton_eliminar_tarea.clicked.connect(self.eliminar_tarea)
        self.ui.boton_completar_tarea.clicked.connect(self.completar_tarea)

    def agregar_tarea(self):
        texto = self.ui.ingreso_tarea.text()
        if texto:
            item = QStandardItem(texto)
            self.modelo_tareas.appendRow(item)
            self.ui.ingreso_tarea.clear()
        else:
            QMessageBox.warning(self, "Error", "El campo de texto está vacío")

    def eliminar_tarea(self):
        tareas = self.ui.tableTareaVacia.currentIndex()
        tareas_completadas = self.ui.tableTareaCompletada.currentIndex()
        if tareas.isValid():
            self.modelo_tareas.removeRow(tareas.row())
        elif tareas_completadas.isValid():
            self.modelo_tareas_completadas.removeRow(tareas_completadas.row())
        else:
            QMessageBox.warning(self, "Error", "Primero selecciona la tarea.")

    def completar_tarea(self):
        tarea_seleccionada = self.ui.tableTareaVacia.currentIndex()
        tarea_completada_seleccionada = self.ui.tableTareaCompletada.currentIndex()

        if tarea_seleccionada.isValid():
            texto_tarea = self.modelo_tareas.itemFromIndex(tarea_seleccionada).text()
            self.modelo_tareas_completadas.appendRow(QStandardItem(texto_tarea))
            self.modelo_tareas.removeRow(tarea_seleccionada.row())
        elif tarea_completada_seleccionada.isValid():
            QMessageBox.warning(self, "Error", "La tarea ya está completada.")
        else:
            QMessageBox.warning(self, "Error", "Primero selecciona la tarea.")

    def iniciar(self):
        self.show()


app = QApplication([])
ventana = Ventana()
ventana.iniciar()
app.exec()
