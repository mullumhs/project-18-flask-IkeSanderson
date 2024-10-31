from flask import Flask, redirect

app = Flask(__name__)



# Our "database" is just a list

todos = ["Beans"]



@app.route('/')

def list_todos():
    tasks = "<ul>"
    # use a loop and <br> to join all to-do's into one string
    for dos in todos:
        tasks += ('<li>' + dos + '</li>')
    # return the to-do list as one string
    return "<h2 style='color: blue'>"+ "To Do" + "</h2>" + "<br>" + tasks + "</ul>"



@app.route('/add/<task>')

def add_todo(task):

    # append the 'task' to the list
    todos.append(task)



    # Return back to the to-do list page

    return redirect('/')



@app.route('/delete/<int:task_id>')

def delete_todo(task_id):

    # delete the item at the specified position in the list
    todos.pop(task_id)

    # Return back to the to-do list page

    return redirect('/')



if __name__ == '__main__':

    app.run(debug=True)