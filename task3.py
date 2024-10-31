from flask import Flask, render_template

app = Flask(__name__)


@app.route('/basic')
def basic():
    return render_template('basic.html')


@app.route('/greet/<name>')
def greet(name):
    return render_template('greet.html', name=name)


@app.route('/inventory/<thing>')
def inventory(thing):
    inventory_items = ['apple', 'banana', 'cherry','balls']
    return render_template('inventory.html', inventory = inventory_items, thing = thing)

@app.route('/test/<message>')
def test(message):

    return render_template('test.html', message = message)

@app.route('/profile/<username>')
def profile(username):

    return render_template('profile.html', username=username)


if __name__ == '__main__':

    app.run(debug=True)