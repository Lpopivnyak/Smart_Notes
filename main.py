from PyQt5.QtWidgets import *

import json

try:
    with open("notes_data.json", "r", encoding="utf-8") as file:
        notes = json.load(file)
except:
    notes = {}

app = QApplication([])
window = QWidget()
window.resize(600, 600)

mainLine = QHBoxLayout()


text = QTextEdit()

notes_Lbl = QLabel("Список заміток")
createNoteButton = QPushButton("Створити замітку")
deleteNoteButton = QPushButton("Видалити замітку")
saveNoteButton = QPushButton("Зберегти замітку")

tags_Lbl = QLabel("Список тегів")
SearchWriteTags = QLineEdit()
addToNoteButton = QPushButton("Додати до замітки")
unfastenFromNoteButton = QPushButton("Відкріпити від заміток")
searchNotes = QPushButton("Шукати замітки по тегу")

listNotes = QListWidget()
listTags = QListWidget()

extraLine1 = QVBoxLayout()
extraLine2 = QVBoxLayout()

app.setStyleSheet("""
        QWidget {
            background: #FFFFFF
    
    
    
    
    
    
            """)

extraLine1.addWidget(text)
mainLine.addLayout(extraLine1)

extraLine2.addWidget(notes_Lbl)
extraLine2.addWidget(listNotes)
extraLine2.addWidget(createNoteButton)
extraLine2.addWidget(deleteNoteButton)
extraLine2.addWidget(saveNoteButton)

extraLine2.addWidget(tags_Lbl)
extraLine2.addWidget(listTags)
extraLine2.addWidget(SearchWriteTags)
extraLine2.addWidget(addToNoteButton)
extraLine2.addWidget(unfastenFromNoteButton)
extraLine2.addWidget(searchNotes)
mainLine.addLayout(extraLine2)

def add_note():
    note_name, ok = QInputDialog.getText(window, "Додати замітку", "Назва замітки: ")
    if ok and note_name != "":
        notes[note_name] = {
            "текст": "",
            "теги": []
        }
        listNotes.clear()
        text.clear()
        listNotes.addItems(notes)

        with open("notes_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, ensure_ascii=False, indent=4)

def save_note():
    if listNotes.selectedItems():
        key = listNotes.selectedItems()[0].text()
        notes[key]["текст"] = text.toPlainText()
        with open("notes_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, ensure_ascii=False)
    else:
        print("Замітка для збереження не вибрана!")

def del_note():
    if listNotes.selectedItems():
        key = listNotes.selectedItems()[0].text()
        notes.pop(key)
        listNotes.clear()
        listTags.clear()
        text.clear()
        listNotes.addItems(notes)
        with open("notes_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, sort_keys=True, ensure_ascii=False, indent=4)
        print(notes)
    else:
        print("Замітка для вилучення не обрана!")
def show_note():
    key = listNotes.selectedItems()[0].text()
    print(key)
    text.setText(notes[key]["текст"])
    listTags.clear()
    listTags.addItems(notes[key]["теги"])

def del_tag(): #кнопка видалити тег
    if listTags.selectedItems():
        key = listNotes.selectedItems()[0].text()
        tag = listTags.selectedItems()[0].text()
        notes[key]["теги"].remove(tag)
        listTags.clear()
        listTags.addItems(notes[key]["теги"])
        with open("notes_data.json", "w", encoding="utf-8") as file:
            json.dump(notes, file, ensure_ascii=False)
    else:
        print("Тег для вилучення не обраний!")


def search_tag(): #кнопка "шукати замітку за тегом"
    button_text = searchNotes.text()
    tag = text.text()

    if button_text == "Шукати замітки за тегом":
        apply_tag_search(tag)
    elif button_text == "Скинути пошук":
        reset_search()

def apply_tag_search(tag):
    notes_filtered = {}
    for note, value in notes.items():
        if tag in value["теги"]:
            notes_filtered[note] = value

    searchNotes.setText("Скинути пошук")
    listNotes.clear()
    listTags.clear()
    listNotes.addItems(notes_filtered)

def reset_search():
    text.clear()
    listNotes.clear()
    listTags.clear()
    listNotes.addItems(notes)
    searchNotes.setText("Шукати замітки за тегом")

createNoteButton.clicked.connect(add_note)
saveNoteButton.clicked.connect(save_note)
deleteNoteButton.clicked.connect(del_note)

listNotes.itemClicked.connect(show_note)


window.setLayout(mainLine)
window.show()
app.exec()