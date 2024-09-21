from PySide6.QtWidgets import QWidget
from ui.ventana_lista_tareas import Ui_Form
from controlador import ConectarBotones


class Ventana(QWidget):
    def __init__(self):
        super().__init__()
        print("Abriendo App")
        self.__ui = Ui_Form()
        self.__ui.setupUi(self)
        self.setWindowTitle("Lista de Tareas")

        # Configuración de la ventana
        self.__ui.tableTareaVacia.horizontalHeader().setVisible(False)
        self.__ui.tableTareaVacia.verticalHeader().setVisible(False)
        self.__ui.tableTareaCompletada.horizontalHeader().setVisible(False)
        self.__ui.tableTareaCompletada.verticalHeader().setVisible(False)
        self.__ui.tableTareaVacia.horizontalHeader().setStretchLastSection(True)
        self.__ui.tableTareaCompletada.horizontalHeader().setStretchLastSection(True)

        # instancio ConectarBotones y paso la ventana a los métodos
        self.__botones_controlador = ConectarBotones(self.__ui)
        self.__ui.boton_agregar_tarea.clicked.connect(self.__botones_controlador.agregar_tarea)
        self.__ui.boton_completar_tarea.clicked.connect(self.__botones_controlador.completar_tarea)
        self.__ui.boton_eliminar_tarea.clicked.connect(self.__botones_controlador.eliminar_tarea)

