from flask import Flask, render_template, request, redirect, url_for
from vault import add_secret, get_secret  # import the functions from your vault logic

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/add_secret', methods=['POST'])
def add_secret_web():
    if request.method == 'POST':
        name = request.form['name']
        value = request.form['value']
        add_secret(name, value)
        return redirect(url_for('index'))

@app.route('/get_secret', methods=['POST'])
def get_secret_web():
    if request.method == 'POST':
        name = request.form['name']
        secret = get_secret(name)
        return render_template('index.html', secret=secret, name=name)

if __name__ == '__main__':
    app.run(debug=True)
