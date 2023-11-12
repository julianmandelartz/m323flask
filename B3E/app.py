from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'Willkommen zur Flask-Applikation!'

# Route für die Verwendung von Lambda-Ausdrücken zur Sortierung
@app.route('/lambda-sorting')
def lambda_sorting():
    # Liste von Wörtern
    words = ['Apple', 'Banana', 'Orange', 'Strawberry', 'Cherry']

    # Sortieren basierend auf der Länge der Wörter mit einem Lambda-Ausdruck
    sorted_words_length = sorted(words, key=lambda x: len(x))

    # Sortieren basierend auf dem letzten Buchstaben der Wörter
    sorted_words_last_letter = sorted(words, key=lambda x: x[-1])

    return f'Sorted by Length: {sorted_words_length}, Sorted by Last Letter: {sorted_words_last_letter}'

if __name__ == '__main__':
    app.run(debug=True)
