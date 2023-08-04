import json
import os
import datetime

FILE_NAME = "notes.json"

def load_notes():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, 'r') as file:
            return json.load(file)
    else:
        return []

def save_notes(notes):
    with open(FILE_NAME, 'w') as file:
        json.dump(notes, file, indent=2)

def create_note():
    title = input("Введите заголовок заметки: ")
    body = input("Введите текст заметки: ")
    timestamp = datetime.datetime.now().isoformat()
    return {"id": len(notes) + 1, "title": title, "body": body, "timestamp": timestamp}

def display_notes(notes):
    if not notes:
        print("Список заметок пуст.")
    else:
        for note in notes:
            print(f"ID: {note['id']}, Заголовок: {note['title']}, Время: {note['timestamp']}")

def find_note_by_id(notes, note_id):
    for note in notes:
        if note['id'] == note_id:
            return note
    return None

def edit_note(notes, note_id):
    for note in notes:
        if note['id'] == note_id:
            new_title = input("Введите новый заголовок заметки: ")
            new_body = input("Введите новый текст заметки: ")
            note['title'] = new_title
            note['body'] = new_body
            note['timestamp'] = datetime.datetime.now().isoformat()
            return True
    return False

def delete_note(notes, note_id):
    for note in notes:
        if note['id'] == note_id:
            notes.remove(note)
            return True
    return False

def filter_notes_by_date(notes, date_str):
    filtered_notes = []
    for note in notes:
        if note['timestamp'].startswith(date_str):
            filtered_notes.append(note)
    return filtered_notes

if __name__ == "__main__":
    notes = load_notes()

    while True:
        print("\nВыберите действие:")
        print("1. Посмотреть список заметок")
        print("2. Создать новую заметку")
        print("3. Редактировать заметку")
        print("4. Удалить заметку")
        print("5. Показать заметки по дате")
        print("6. Выйти")

        choice = input("Введите номер действия: ")

        if choice == "1":
            display_notes(notes)
        elif choice == "2":
            new_note = create_note()
            notes.append(new_note)
            save_notes(notes)
            print("Заметка успешно создана.")
        elif choice == "3":
            note_id = int(input("Введите ID заметки для редактирования: "))
            if edit_note(notes, note_id):
                save_notes(notes)
                print("Заметка успешно отредактирована.")
            else:
                print("Заметка с указанным ID не найдена.")
        elif choice == "4":
            note_id = int(input("Введите ID заметки для удаления: "))
            if delete_note(notes, note_id):
                save_notes(notes)
                print("Заметка успешно удалена.")
            else:
                print("Заметка с указанным ID не найдена.")
        elif choice == "5":
            date_str = input("Введите дату (гггг-мм-дд), для вывода заметок за эту дату: ")
            filtered_notes = filter_notes_by_date(notes, date_str)
            if filtered_notes:
                print("Заметки за указанную дату:")
                display_notes(filtered_notes)
            else:
                print("Заметки за указанную дату не найдены.")
        elif choice == "6":
            print("Программа завершена.")
            break
        else:
            print("Некорректный ввод. Повторите попытку.")