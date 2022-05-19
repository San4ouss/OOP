class Notebook:
    def __init__(self, *args):
        self._notes = args

    @property
    def notes_list(self):
        for i, j in enumerate(self._notes[0]):
            print(f'{i + 1}.{j}')


note = Notebook(['Buy Potato', 'Buy Carrot', 'Wash car'])
note.notes_list
