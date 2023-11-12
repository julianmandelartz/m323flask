from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Willkommen zur Flask-Applikation!'

# Beispiel für Implementierung zusammenhängender Funktionen zu einem Algorithmus
@app.route('/connected-functions')
def connected_functions():
    # Beispiel für die Implementierung zusammenhängender Funktionen in einem Algorithmus
    def step_one(data):
        # Schritt 1
        return data * 2

    def step_two(data):
        # Schritt 2
        return data + 10

    def main_algorithm(data):
        result_step_one = step_one(data)
        result_step_two = step_two(result_step_one)
        return f'Result: {result_step_two}'

    return main_algorithm(5)  # Beispielaufruf mit Daten

if __name__ == '__main__':
    app.run(debug=True)
