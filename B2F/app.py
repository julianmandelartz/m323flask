from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Willkommen zur Flask-Applikation!'

# Beispiel zur Verwendung von Funktionen als Argumente
@app.route('/function-arguments')
def function_arguments():
    # Beispiel zur Verwendung von Funktionen als Argumente
    def apply_operation(operation, x, y):
        return operation(x, y)

    # Beispiel-Funktionen, die als Argument verwendet werden
    def add(a, b):
        return a + b

    def multiply(a, b):
        return a * b

    result_addition = apply_operation(add, 3, 4)
    result_multiplication = apply_operation(multiply, 3, 4)

    return f'Result Addition: {result_addition}, Result Multiplication: {result_multiplication}'

if __name__ == '__main__':
    app.run(debug=True)
