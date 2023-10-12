import sys
from PyQt6.QtWidgets import (
    QApplication,
    QWidget,
    QFileDialog,
    QGridLayout,
    QPushButton,
    QLabel,
    QListWidget,
    QLineEdit,
)
from pathlib import Path


class EmptyWindow(QWidget):
    def __init__(self):
        super().__init__()
        self.initializeUI()

    def initializeUI(self):
        self.setGeometry(100, 100, 1000, 600)
        self.setWindowTitle("Astro Viewer")
        self.show()


class MainWindow(QWidget):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        # setup window
        self.setWindowTitle("PyQt File Dialog")
        self.setGeometry(100, 100, 400, 100)
        layout = QGridLayout()
        self.setLayout(layout)

        # button to open file selection widget
        browse_button = QPushButton("Browse")
        browse_button.clicked.connect(self.handle_open_file_dialog)
        self.filename_edit = QLineEdit()

        # button to open image viewing window
        open_button = QPushButton("Open")

        # add components to the layout
        layout.addWidget(QLabel("File:"), 0, 0)
        layout.addWidget(self.filename_edit, 0, 1)
        layout.addWidget(browse_button, 0, 2)
        layout.addWidget(open_button, 1, 2)

        # add handlers
        open_button.clicked.connect(self.handle_open_image)

        self.show()

    def handle_open_file_dialog(self):
        filename, ok = QFileDialog.getOpenFileName(
            self, "Select a File", ".", "Images (*.png *.jpg *.jpeg *.fits)"
        )
        if filename:
            path = Path(filename)
            self.filename_edit.setText(str(path))

    def handle_open_image(self):
        print(self.filename_edit.text())


if __name__ == "__main__":
    print("Test")
    app = QApplication(sys.argv)
    window = MainWindow()
    sys.exit(app.exec())
