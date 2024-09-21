from PySide6.QtWidgets import QApplication
import sys
from ventana import Ventana

if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = Ventana()
    ventana.show()
    sys.exit(app.exec())




