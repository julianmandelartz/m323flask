from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Willkommen zur Flask-Applikation!'

# Beispiel zum Umgang mit Funktionen als Objekte
@app.route('/function-objects')
def function_objects():
    # Beispiel zur Behandlung von Funktionen als Objekte
    def greet():
        return 'Hello!'

    def farewell():
        return 'Goodbye!'

    # Funktion in einer Variablen speichern und aufrufen
    my_function = greet
    result = my_function()

    return f'Result: {result}'  # Beispielaufruf und Ergebnis

if __name__ == '__main__':
    app.run(debug=True)
