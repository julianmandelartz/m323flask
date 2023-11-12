from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Willkommen zur Flask-Applikation!'

# Beispiel für unterschiedliche Lösungsansätze in den Paradigmen
@app.route('/paradigm-solutions')
def paradigm_solutions():
    # Codebeispiel für unterschiedliche Lösungsansätze in den Paradigmen
    # Beispiel für OO-Lösung
    class Animal:
        def __init__(self, species):
            self.species = species

        def make_sound(self):
            pass  # Methode variiert je nach Unterklasse

    class Dog(Animal):
        def make_sound(self):
            return "Bark!"

    # Beispiel für prozedurale Lösung
    def greet():
        return "Hello!"

    # Beispiel für funktionale Lösung
    def double(x):
        return x * 2

    return f'Beispiel für OO-Lösung: {Dog().make_sound()}, Prozedurale Lösung: {greet()}, Funktionale Lösung: {double(5)}'

if __name__ == '__main__':
    app.run(debug=True)
