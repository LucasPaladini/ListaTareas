from PySide6.QtWidgets import QApplication
from ventana import Ventana
import sys

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())
    