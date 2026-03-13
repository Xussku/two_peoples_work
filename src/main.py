# src/main.py
def main():
    while True:
        print("\n--- Менеджер заметок ---")
        print("1. Добавить заметку")
        print("2. Показать все заметки")
        print("3. Удалить заметку по ID")
        print("4. Выход")

        choice = input("Выберите действие: ")

        if choice == '1':
            print("Заглушка: Здесь будет добавление заметки.")
        elif choice == '2':
            print("Заглушка: Здесь будет показ всех заметок.")

        elif choice == '3':
            try:
                note_id = int(input("Введите ID заметки для удаления: "))
                print(f"Заглушка: Здесь будет удаление заметки с ID {note_id}.")
            except ValueError:
                print("Ошибка: Введите число.")

        elif choice == '4':
            print("До свидания!")
            break
        else:
            print("Неверный ввод. Попробуйте снова.")

if __name__ == "__main__":
    main()