from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Willkommen zur Flask-Applikation!'

# Funktionaler Ansatz für Algorithmuserklärung
@app.route('/functional-algorithm')
def functional_algorithm():
    # Codebeispiel für algorithmische Lösung mit funktionalem Ansatz
    def factorial(n):
        if n == 0:
            return 1
        else:
            return n * factorial(n - 1)

    return f'Beispiel für funktionalen Algorithmus: Fakultät von 5 ist {factorial(5)}'

if __name__ == '__main__':
    app.run(debug=True)
