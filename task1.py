from flask import Flask

task1 = Flask(__name__)

@task1.route('/')

def index():

    return 'Hello, World!'

@task1.route('/hello/<name>')

def hello(name):

    return f'Hello, {name}!'

if __name__ == '__main__':

    task1.run(debug=True)
   