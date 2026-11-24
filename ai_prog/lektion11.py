from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QLineEdit, QVBoxLayout, QWidget, QFileDialog, QLabel

app = QApplication([])

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("My App")


        # init buttons
        self.selectButton = QPushButton("Open File Dialog", self)

        self.updateButton = QPushButton("Update Textbox", self) 

        self.textbox = QLineEdit(self)

        self.wordCount = QLabel("Word Count: 0", self)



        # init button methods
        self.selectButton.clicked.connect(self.button_clicked)
        self.updateButton.clicked.connect(self.update_textbox)

        # layout
        layout = QVBoxLayout()
        layout.addWidget(self.selectButton)
        layout.addWidget(self.updateButton)
        layout.addWidget(self.textbox)
        layout.addWidget(self.wordCount)

        # set widget
        central_widget = QWidget()
        central_widget.setLayout(layout)
        self.setCentralWidget(central_widget)


    def button_clicked(self):
        # open file dialog
        dialog = QFileDialog(self)
        dialog.setFileMode(QFileDialog.FileMode.ExistingFile) # only one file
        dialog.setNameFilter("Text files (*.txt)") # only text files
        dialog.setViewMode(QFileDialog.ViewMode.List) 

        if dialog.exec():
            filenames = dialog.selectedFiles()
            if filenames:
                filename = filenames[0] # get the first file

                # read the file and display its content in the textbox
                with open(filename, "r", encoding="utf-8") as file:
                    content = file.read()

                print(content)
                self.textbox.setText(content)
                self.update_word_count()
                self.filename = filename

    def update_textbox(self):
        # when pressed update the file
        if hasattr(self, "filename"):
            with open(self.filename, "w", encoding="utf-8") as file:
                file.write(self.textbox.text())

            self.update_word_count()

    def update_word_count(self):
        text = self.textbox.text()
        word_count = len(text.split())
        self.wordCount.setText(f"Word Count: {word_count}")

window = MainWindow()

window.show()

app.exec()
