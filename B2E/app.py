from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Willkommen zur Flask-Applikation!'

# Beispiel zur Verwendung von Funktionen als Objekte in Closures
@app.route('/function-closures')
def function_closures():
    # Beispiel zur Verwendung von Funktionen als Objekte in Closures
    def outer_function(x):
        def inner_function(y):
            return x + y
        return inner_function

    # Closure mit Funktionen als Objekte
    closure = outer_function(5)
    result = closure(3)

    return f'Result: {result}'  # Ergebnis der Closure-Anwendung

if __name__ == '__main__':
    app.run(debug=True)
