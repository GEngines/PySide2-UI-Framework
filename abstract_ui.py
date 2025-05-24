import sys
from PySide2.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QAction, QMenu
)
from PySide2 import QtWidgets, QtCore

def load_stylesheet(path):
    try:
        with open(path, "r") as f:
            return f.read()
    except Exception as e:
        print(f"Failed to load stylesheet {path}: {e}")
        return ""

class AbstractAdvancedUI(QMainWindow):
    """
    Pseudo-abstract PySide2 MainWindow with theme switching and extensible UI.
    Subclass this and implement add_custom_widgets(self, layout)
    to add your own widgets to the central layout.
    """
    def __init__(self, theme="light"):
        super().__init__()
        self.setWindowTitle("Advanced PySide2 Abstract UI")
        self.setGeometry(100, 100, 800, 600)
        self.theme = theme
        self.theme_paths = {
            "light": "resources/styles/light.css",
            "dark": "resources/styles/dark.css"
        }

        self.menu_bar = self.menuBar()
        self._setup_menus()

        toolbar = QtWidgets.QToolBar("Main Toolbar")
        toolbar.addAction("Toolbar Action")
        self.addToolBar(toolbar)

        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Call method for subclass-specific widgets
        self.add_custom_widgets(layout)

        self.statusBar().showMessage("Ready")
        self.apply_theme(self.theme)

    def _setup_menus(self):
        file_menu = self.menu_bar.addMenu("File")
        file_menu.addAction("Open")
        file_menu.addAction("Save")
        file_menu.addAction("Exit", self.close)

        edit_menu = self.menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Paste")

        theme_menu = QMenu("Theme", self)
        light_action = QAction("Light", self)
        dark_action = QAction("Dark", self)
        light_action.setCheckable(True)
        dark_action.setCheckable(True)
        light_action.setChecked(self.theme == "light")
        dark_action.setChecked(self.theme == "dark")
        theme_menu.addAction(light_action)
        theme_menu.addAction(dark_action)
        self.menu_bar.addMenu(theme_menu)

        action_group = QtWidgets.QActionGroup(self)
        action_group.addAction(light_action)
        action_group.addAction(dark_action)

        light_action.triggered.connect(lambda: self.apply_theme("light"))
        dark_action.triggered.connect(lambda: self.apply_theme("dark"))

    def apply_theme(self, theme_name):
        if theme_name not in self.theme_paths:
            print(f"Theme {theme_name} not found")
            return
        qss = load_stylesheet(self.theme_paths[theme_name])
        self.theme = theme_name
        QApplication.instance().setStyleSheet(qss)

    def add_custom_widgets(self, layout):
        """
        Override this in subclasses to add custom widgets to the central layout.
        """
        raise NotImplementedError("Subclasses must implement add_custom_widgets(layout)")
