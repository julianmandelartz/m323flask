from flask import Flask, render_template

app = Flask(__name__)

# Startseite
@app.route('/')
def index():
    return 'Willkommen zur Startseite!'

# Eine weitere Seite
@app.route('/about')
def about():
    return 'Über uns'

# Template basierte Seite
@app.route('/user/<name>')
def user(name):
    return render_template('user.html', name=name)

# 404 Error-Handler
@app.errorhandler(404)
def page_not_found(error):
    return 'Diese Seite existiert nicht.', 404

if __name__ == '__main__':
    app.run(debug=True)
