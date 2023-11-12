from flask import Flask
from functools import reduce

app = Flask(__name__)

@app.route('/')
def index():
    return 'Willkommen zur Flask-Applikation!'

@app.route('/complex-data-processing')
def complex_data_processing():
    data = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

    aggregated_data = reduce(
        lambda acc, sublist: acc + list(map(lambda x: x * 2, filter(lambda x: x % 2 == 0, sublist))),
        data,
        []
    )

    return f'Aggregated Data: {aggregated_data}'

if __name__ == '__main__':
    app.run(debug=True)
