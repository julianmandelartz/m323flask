from flask import Flask

app = Flask(__name__)

# Vor Refactoring
@app.route('/complex-function')
def complex_function_route():
    data = [1, 2, 3, 4, 5]
    result = sum(data)
    if result > 10 and result % 2 == 0:
        return 'Result is greater than 10 and even'
    elif result > 5:
        return 'Result is greater than 5'
    else:
        return 'Result is unknown'

# Nach Refactoring
@app.route('/refactored-function')
def refactored_function():
    data = [1, 2, 3, 4, 5]
    result = sum(data)
    return display_result_info(result)

def display_result_info(result):
    if result > 10 and result % 2 == 0:
        return 'Result is greater than 10 and even'
    elif result > 5:
        return 'Result is greater than 5'
    else:
        return 'Result is unknown'

if __name__ == '__main__':
    app.run(debug=True)
