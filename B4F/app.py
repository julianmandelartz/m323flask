from flask import Flask
from functools import reduce

app = Flask(__name__)

@app.route('/')
def index():
    return 'Willkommen zur Flask-Applikation!'

@app.route('/combined-map-filter-reduce')
def combined_map_filter_reduce():
    words = ['Apple', 'Banana', 'Cherry', 'Date']

    processed_data = reduce(
        lambda acc, word: acc + word.upper(),
        filter(lambda word: len(word) > 5, map(lambda word: word.lower(), words)),
        ''
    )

    return f'Processed Data: {processed_data}'

if __name__ == '__main__':
    app.run(debug=True)
