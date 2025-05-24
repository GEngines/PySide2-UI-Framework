import sys
from PySide2.QtWidgets import (
    QApplication, QWidget, QVBoxLayout, QLabel, QPushButton,
    QLineEdit, QComboBox, QTableWidget, QProgressBar,
    QTabWidget, QSlider, QCheckBox, QRadioButton, QSpinBox, QCalendarWidget
)
from PySide2 import QtCore
from abstract_ui import AbstractAdvancedUI

class AdvancedUI(AbstractAdvancedUI):
    def add_custom_widgets(self, layout):
        layout.addWidget(QLabel("Welcome to your standardized UI!"))

        btn = QPushButton("Standard Button")
        btn.setObjectName("CustomButton")
        layout.addWidget(btn)

        line_edit = QLineEdit()
        line_edit.setPlaceholderText("Type here...")
        layout.addWidget(line_edit)

        combo = QComboBox()
        combo.addItems(["Option 1", "Option 2", "Option 3"])
        layout.addWidget(combo)

        table = QTableWidget(3, 3)
        table.setHorizontalHeaderLabels(["A", "B", "C"])
        layout.addWidget(table)

        progress = QProgressBar()
        progress.setValue(50)
        layout.addWidget(progress)

        tabs = QTabWidget()
        tab1 = QWidget()
        tab1_layout = QVBoxLayout()
        tab1.setLayout(tab1_layout)
        tab1_layout.addWidget(QLabel("Tab 1 content"))
        tab2 = QWidget()
        tab2_layout = QVBoxLayout()
        tab2.setLayout(tab2_layout)
        tab2_layout.addWidget(QLabel("Tab 2 content"))
        tabs.addTab(tab1, "Tab 1")
        tabs.addTab(tab2, "Tab 2")
        layout.addWidget(tabs)

        slider = QSlider(QtCore.Qt.Horizontal)
        layout.addWidget(slider)

        checkbox = QCheckBox("Check me")
        layout.addWidget(checkbox)

        radio = QRadioButton("Radio button")
        layout.addWidget(radio)

        spinbox = QSpinBox()
        layout.addWidget(spinbox)

        calendar = QCalendarWidget()
        layout.addWidget(calendar)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdvancedUI()
    window.show()
    sys.exit(app.exec_())