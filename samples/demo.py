
import sys

from abstract_ui import AbstractAdvancedUI
from PySide2 import QtWidgets


if __name__ == "__main__":
    class DemoUI(AbstractAdvancedUI):
        def add_custom_widgets(self, layout):
            layout.addWidget(QtWidgets.QLabel("Welcome to your custom UI!"))
            btn = QtWidgets.QPushButton("Standard Button")
            layout.addWidget(btn)
            layout.addWidget(QtWidgets.QLineEdit("Type here..."))

    app = QtWidgets.QApplication(sys.argv)
    window = DemoUI()
    window.show()
    sys.exit(app.exec_())