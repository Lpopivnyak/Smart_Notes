from PyQt5.QtWidgets import *

app = QApplication([])
window = QWidget()
window.resize(600, 600)

mainLine = QHBoxLayout()


text = QTextEdit()

notes = QLabel("Список заміток")
createNoteButton = QPushButton("Створити замітку")
deleteNoteButton = QPushButton("Видалити замітку")
saveNoteButton = QPushButton("Зберегти замітку")

tags = QLabel("Список тегів")
SearchWriteTags = QLineEdit()
addToNoteButton = QPushButton("Додати до замітки")
unfastenFromNoteButton = QPushButton("Відкріпити від заміток")
searchNotes = QPushButton("Шукати замітки по тегу")

listNotes = QListWidget()


extraLine1 = QVBoxLayout()
extraLine2 = QVBoxLayout()


extraLine1.addWidget(text)
mainLine.addLayout(extraLine1)

extraLine2.addWidget(notes)
extraLine2.addWidget(listNotes)
extraLine2.addWidget(createNoteButton)
extraLine2.addWidget(deleteNoteButton)
extraLine2.addWidget(saveNoteButton)

extraLine2.addWidget(tags)
extraLine2.addWidget(listNotes)
extraLine2.addWidget(SearchWriteTags)
extraLine2.addWidget(addToNoteButton)
extraLine2.addWidget(unfastenFromNoteButton)
extraLine2.addWidget(searchNotes)
mainLine.addLayout(extraLine2)


window.setLayout(mainLine)
window.show()
app.exec()