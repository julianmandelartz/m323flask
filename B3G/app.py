from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Willkommen zur Flask-Applikation!'

# Beispiele für einfache Lambda-Ausdrücke
@app.route('/lambda-expressions')
def lambda_expressions():
    # Lambda-Ausdruck für das Quadrieren einer Zahl
    square = lambda x: x ** 2

    # Lambda-Ausdruck für das Konvertieren eines Strings in Großbuchstaben
    uppercase = lambda s: s.upper()

    result_square = square(5)
    result_uppercase = uppercase('hello')

    return f'Result Square: {result_square}, Result Uppercase: {result_uppercase}'

if __name__ == '__main__':
    app.run(debug=True)
