#!/usr/bin/python
import sqlite3
import bottle
from bottle import Bottle, route, run, debug, template, request, static_file, error, redirect
from export_task import export_excel


todo = application = bottle.Bottle()
# only needed when you run Bottle on mod_wsgi
from bottle import default_app

dbdir = str('todo.db')

@todo.route('/')
def root_page():
    redirect('/todo')

@todo.route('/todo')
def todo_list():
    conn = sqlite3.connect(dbdir)
    c = conn.cursor()
    c.execute("SELECT id, task, taskdescr, score FROM todo WHERE status LIKE '1' order by score asc")
    result = c.fetchall()
    c.close()

    output = template('make_table', rows=result)
    return output

@todo.route('/todo/closedtask')
def closed_task():

    conn = sqlite3.connect(dbdir)
    c = conn.cursor()
    c.execute("SELECT id, task, taskdescr, score FROM todo where status Like '0';")
    result = c.fetchall()
    c.close()

    output = template('closedtask', rows=result)
    return output


@todo.route('/todo/new', method='GET')
def new_item():

    if request.GET.get('save','').strip():

        taskentry = request.GET.get('task', '').strip()
        taskdescrentry = request.GET.get('taskdescr', ''.strip())
        scoreentry = request.GET.get('taskscore', ''.strip())
        conn = sqlite3.connect(dbdir)
        c = conn.cursor()

        c.execute("INSERT INTO todo (task,taskdescr,score,status) VALUES (?,?,?,?)", (taskentry,taskdescrentry, scoreentry,1))
        new_id = c.lastrowid

        conn.commit()
        c.close()

        return '<p>The new task was inserted into the database, the ID is %s</p>' % new_id, '<a href="/todo">Return to Todo List</a>'

    else:
        return template('new_task.tpl')

@todo.route('/todo/edit/:no', method='GET')
def edit_item(no):

    if request.GET.get('save','').strip():
        edit = request.GET.get('task','').strip()
        editdescr = request.GET.get('taskdescr','').strip()
        editscore = request.GET.get('taskscore','').strip()
        status = request.GET.get('status','').strip()

        if status == 'open':
            status = 1
        else:
            status = 0

        conn = sqlite3.connect(dbdir)
        c = conn.cursor()
        c.execute("UPDATE todo SET task = ?,taskdescr = ?,score = ?, status = ? WHERE id LIKE ?;", (edit,editdescr,editscore,status,no))
        conn.commit()

        return '<p>The item number %s was successfully updated</p>' %no, '<a href="/todo">Return to Todo List</a>'

    else:
        conn = sqlite3.connect(dbdir)
        c = conn.cursor()
        c.execute("SELECT task, taskdescr FROM todo WHERE id LIKE ?;", [no])
        cur_data = c.fetchone()

        return template('edit_task', old = cur_data, no = no)

@todo.route('/todo/item:item#[0-9]+#')
def show_item(item):

        conn = sqlite3.connect(dbdir)
        c = conn.cursor()
        c.execute("SELECT task FROM todo WHERE id LIKE ?", (item))
        result = c.fetchall()
        c.close()

        if not result:
            return 'This item number does not exist!'
        else:
            return 'Task: %s' %result[0]

@todo.route('/todo/help')
def help():

    static_file('help.html', root='.')

@todo.route('/todo/json:json#[0-9]+#')
def show_json(json):

    conn = sqlite3.connect(dbdir)
    c = conn.cursor()
    c.execute("SELECT task FROM todo WHERE id LIKE ?", (json))
    result = c.fetchall()
    c.close()

    if not result:
        return {'task':'This item number does not exist!'}
    else:
        return {'Task': result[0]}

@todo.route('/todo/download/<filename:path>')
def download(filename):
    export_excel()
    return static_file(filename, root='./download', download=filename)


@todo.route('/todo/testnum/:no', method='GET')
def edit_item(no):
    return '<p>As a integer %s</p>' %no, '<p>As a string %s</p>' %(str(no))


@error(403)
def mistake403(code):
    return 'There is a mistake in your url!'

@error(404)
def mistake404(code):
    return 'Sorry, this page does not exist!'


#debug(True)
todo.run(reloader=True, host='localhost', port=9393)
#remember to remove reloader=True and debug(True) when you mohost='localhost', port=8080ve your application from development to a productive environment
