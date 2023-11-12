from flask import Flask, render_template

app = Flask(__name__)

@app.route('/immutable')
def immutable_example():
    immutable_value = "Hallo"
    immutable_value += " Welt"  # Eine Veränderung führt zur Erstellung eines neuen Objekts
    return render_template('immutable.html', value=immutable_value)

@app.route('/mutable')
def mutable_example():
    mutable_list = [1, 2, 3]
    mutable_list.append(4)  # Die Liste wird verändert, nicht neu erstellt
    return render_template('mutable.html', value=mutable_list)

if __name__ == '__main__':
    app.run(debug=True)
