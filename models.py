import json


class Todos:
    def __init__(self):
        try:
            with open("todos.json", "r", encoding="UTF-8") as f:
                self.todos = json.load(f)
        except FileNotFoundError:
            self.todos = []

    def all(self):
        return self.todos

    def get(self, id):
        return self.todos[id]

    def create(self, data):
        data.pop('csrf_token')
        self.todos.append(data)

    def save_all(self):
        with open("todos.json", "w", encoding="UTF-8") as f:
            json.dump(self.todos, f, ensure_ascii=False)

    def update(self, id, data):
        data.pop('csrf_token')
        self.todos[id] = data
        self.save_all()


todos = Todos()


