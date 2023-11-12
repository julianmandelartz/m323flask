from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Willkommen zur Flask-Applikation!'

# Lambda-Ausdrücke mit mehreren Argumenten
@app.route('/multi-argument-lambda')
def multi_argument_lambda():
    # Lambda-Ausdruck für die Addition zweier Zahlen
    addition = lambda x, y: x + y

    result = addition(3, 5)

    return f'Result Addition: {result}'

if __name__ == '__main__':
    app.run(debug=True)
