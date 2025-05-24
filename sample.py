import sys
from PySide2.QtWidgets import (
    QApplication, QMainWindow, QWidget, QVBoxLayout, QAction, QMenu
)
from PySide2 import QtWidgets, QtCore

def load_stylesheet(path):
    """Load a QSS stylesheet from the given file path."""
    try:
        with open(path, "r") as f:
            return f.read()
    except Exception as e:
        print(f"Failed to load stylesheet {path}: {e}")
        return ""  # Fallback to no stylesheet if file missing

class AdvancedUI(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Advanced PySide2 UI (Python Only)")
        self.setGeometry(100, 100, 800, 600)
        self.theme = "light"  # Default theme
        self.theme_paths = {
            "light": "resources/styles/light.css",
            "dark": "resources/styles/dark.css"
        }

        # Menu bar (supports QMenu, QMenuBar, QActions, etc.)
        self.menu_bar = self.menuBar()
        self._setup_menus()

        # Tool bar
        toolbar = QtWidgets.QToolBar("Main Toolbar")
        toolbar.addAction("Toolbar Action")
        self.addToolBar(toolbar)

        # Central widget and layout
        central_widget = QWidget()
        layout = QVBoxLayout()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)

        # Example widgets from various PySide2 modules
        layout.addWidget(QtWidgets.QLabel("Welcome to your standardized UI!"))

        # QPushButton
        btn = QtWidgets.QPushButton("Standard Button")
        btn.setObjectName("CustomButton")
        layout.addWidget(btn)

        # QLineEdit
        line_edit = QtWidgets.QLineEdit()
        line_edit.setPlaceholderText("Type here...")
        layout.addWidget(line_edit)

        # QComboBox
        combo = QtWidgets.QComboBox()
        combo.addItems(["Option 1", "Option 2", "Option 3"])
        layout.addWidget(combo)

        # QTableWidget
        table = QtWidgets.QTableWidget(3, 3)
        table.setHorizontalHeaderLabels(["A", "B", "C"])
        layout.addWidget(table)

        # QProgressBar
        progress = QtWidgets.QProgressBar()
        progress.setValue(50)
        layout.addWidget(progress)

        # QTabWidget
        tabs = QtWidgets.QTabWidget()
        tab1 = QWidget()
        tab1_layout = QVBoxLayout()
        tab1.setLayout(tab1_layout)
        tab1_layout.addWidget(QtWidgets.QLabel("Tab 1 content"))
        tab2 = QWidget()
        tab2_layout = QVBoxLayout()
        tab2.setLayout(tab2_layout)
        tab2_layout.addWidget(QtWidgets.QLabel("Tab 2 content"))
        tabs.addTab(tab1, "Tab 1")
        tabs.addTab(tab2, "Tab 2")
        layout.addWidget(tabs)

        # QSlider
        slider = QtWidgets.QSlider(QtCore.Qt.Horizontal)
        layout.addWidget(slider)

        # QCheckBox
        checkbox = QtWidgets.QCheckBox("Check me")
        layout.addWidget(checkbox)

        # QRadioButton
        radio = QtWidgets.QRadioButton("Radio button")
        layout.addWidget(radio)

        # QSpinBox
        spinbox = QtWidgets.QSpinBox()
        layout.addWidget(spinbox)

        # QCalendarWidget
        calendar = QtWidgets.QCalendarWidget()
        layout.addWidget(calendar)

        # Status bar
        self.statusBar().showMessage("Ready")

        # Apply the initial theme
        self.apply_theme(self.theme)

    def _setup_menus(self):
        file_menu = self.menu_bar.addMenu("File")
        file_menu.addAction("Open")
        file_menu.addAction("Save")
        file_menu.addAction("Exit", self.close)

        edit_menu = self.menu_bar.addMenu("Edit")
        edit_menu.addAction("Copy")
        edit_menu.addAction("Paste")

        # Theme menu for switching at runtime
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

        # Group actions so only one can be checked
        action_group = QtWidgets.QActionGroup(self)
        action_group.addAction(light_action)
        action_group.addAction(dark_action)

        light_action.triggered.connect(lambda: self.apply_theme("light"))
        dark_action.triggered.connect(lambda: self.apply_theme("dark"))

    def apply_theme(self, theme_name):
        """Switch stylesheet at runtime."""
        if theme_name not in self.theme_paths:
            print(f"Theme {theme_name} not found")
            return
        qss = load_stylesheet(self.theme_paths[theme_name])
        self.theme = theme_name
        QApplication.instance().setStyleSheet(qss)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = AdvancedUI()
    window.show()
    sys.exit(app.exec_())