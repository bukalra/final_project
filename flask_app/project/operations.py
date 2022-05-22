import json

class Todos:
    def __init__(self):
        try:
            with open("USIAD02_Config.Json", "r") as f:
                self.todos = json.load(f)
                print('==================udao sie ')
        except FileNotFoundError:
            print('==================nie udao sie ')
            self.todos = []

    def all(self):
        return self.todos

    def get(self, name):
        todo = [todo for todo in self.all()['Calling Huntgroups'] if todo['name'] == name]
        if todo:
            return todo[0]
        return []

    def create(self, data):
        # data.pop('csrf_token')
        self.todos['Calling Huntgroups'].append(data)
        self.save_all()

    def save_all(self):
        with open("todos.json", "w") as f:

            json.dump(self.todos, f)



    def update(self, name, data):
        todo = self.get(name)
        
        if todo:
            index = self.todos['Calling Huntgroups'].index(todo)
            # data.pop('csrf_token')

            self.todos['Calling Huntgroups'][index] = data
            self.save_all()
            return True
        return False
        
    def delete(self, id):
        todo = self.get(id)
        if todo:
            self.todos.remove(todo)
            self.save_all()
            return True
        return False

todos = Todos()
