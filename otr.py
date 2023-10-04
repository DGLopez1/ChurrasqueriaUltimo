
from PyQt5.QtWidgets import QApplication, QMainWindow, QLabel, QPushButton
import sys
from PyQt5.QtGui import QPixmap


class RestaurantInterface(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Restaurante")
        self.setGeometry(100, 100, 500, 400)

        self.label1 = QLabel(self)
        self.label1.setGeometry(0, 0, 800, 600)
        self.label1.setPixmap(QPixmap("./images/background.png"))

        # Crear etiqueta de fondo
       

        # Botón "Añadir a Pedido"
        add_button = QPushButton("Añadir a Pedido", self)
        add_button.setGeometry(50, 50, 150, 50)
        add_button.setStyleSheet("background-color: #ffffff; color: #000000; font-size: 16px;")

        # Botón "Realizar Pedido"
        order_button = QPushButton("Realizar Pedido", self)
        order_button.setGeometry(200, 150, 150, 50)
        order_button.setStyleSheet("background-color: #ffffff; color: #000000; font-size: 16px;")

        # Botón "Entrega"
        delivery_button = QPushButton("Entrega", self)
        delivery_button.setGeometry(350, 250, 150, 50)
        delivery_button.setStyleSheet("background-color: #ffffff; color: #000000; font-size: 16px;")

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = RestaurantInterface()
    window.show()
    sys.exit(app.exec_())
