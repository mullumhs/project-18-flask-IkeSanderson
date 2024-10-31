from flask import Flask, request

app = Flask(__name__)

@app.route('/')
def index():
    return 'Hello, World!'

@app.route('/hello/<name>')

def hello(name):

    return f'Hello, {name}!'

@app.route('/calc/<int:num1>/<string:operation>/<int:num2>')
def calculator(num1, operation, num2):

    if operation == "+":
        result = num1 + num2
    elif operation =="-":
        result = num1 - num2
    return f'{num1} {operation} {num2} = {result}'

@app.route('/search')

def search():

    query = request.args.get('q', '')

    category = request.args.get('category', 'all')

    return f'Searching for "{query}" in category: {category}'

if __name__ == '__main__':

    app.run(debug=True)
   