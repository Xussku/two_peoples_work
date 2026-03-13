class NoteStorage:
    def __init__(self):
        self.notes = []
        self.counter = 1

    def add_note(self, title, body):
        note = {'id': self.counter, 'title': title, 'body': body}
        self.notes.append(note)
        self.counter += 1
        print(f"Заметка {note['id']} добавлена")

    def get_all_notes(self):
        return self.notes

    def remove_note(self, note_id):
        for note in self.notes:
            if note['id'] == note_id:
                self.notes.remove(note)
                print(f"Заметка с ID {note_id} удалена!")
                return True
        print(f"Заметка с ID {note_id} не найдена.")
        return False