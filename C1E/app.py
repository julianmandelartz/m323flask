from flask import Flask

app = Flask(__name__)

def calculate(data):
    return sum(data)

def display_info(result):
    if result > 10 and result % 2 == 0:
        return 'Result is greater than 10 and even'
    elif result > 5:
        return 'Result is greater than 5'
    else:
        return 'Result is unknown'

@app.route('/refactored_function')
def refactored_function():
    data = [1, 2, 3, 4, 5]
    result = calculate(data)
    return display_info(result)

if __name__ == '__main__':
    app.run(debug=True)
