from flask import Flask
from functools import reduce

app = Flask(__name__)

@app.route('/')
def index():
    return 'Willkommen zur Flask-Applikation!'

@app.route('/map-filter-reduce')
def map_filter_reduce():
    numbers = [1, 2, 3, 4, 5]

    squared_numbers = list(map(lambda x: x ** 2, numbers))
    even_numbers = list(filter(lambda x: x % 2 == 0, numbers))
    sum_of_numbers = reduce(lambda x, y: x + y, numbers)

    return f'Squared Numbers: {squared_numbers}, Even Numbers: {even_numbers}, Sum of Numbers: {sum_of_numbers}'

if __name__ == '__main__':
    app.run(debug=True)
