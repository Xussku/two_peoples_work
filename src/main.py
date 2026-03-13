from defs import NoteStorage

def main():
    storage = NoteStorage()

    while True:
        print()
        print("--- Менеджер заметок ---")
        print("1. Добавить заметку")
        print("2. Показать все заметки")
        print("3. Удалить заметку по ID")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            title = input("Введите заголовок: ")
            body = input("Введите текст заметки: ")
            storage.add_note(title, body)

        elif choice == '2':
            notes = storage.get_all_notes()
            if not notes:
                print("Заметок нет")
            else:
                for note in notes:
                    print(f"[ID: {note['id']}] {note['title']} - {note['body']}")

        elif choice == '3':
            try:
                note_id = int(input("Введите ID заметки для удаления: "))
                storage.remove_note(note_id)
            except ValueError:
                print("Ошибка")

        elif choice == '4':
            print("выход")
            break
        else:
            print("Неверный ввод")

if __name__ == "__main__":
    main()