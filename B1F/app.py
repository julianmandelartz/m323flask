from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Willkommen zur Flask-Applikation!'

# Beispiel für Zerlegung von Algorithmen in funktionale Teile
@app.route('/functional-parts')
def functional_parts():
    # Beispiel für die Zerlegung eines Algorithmus in funktionale Teile
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
