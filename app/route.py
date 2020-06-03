from . import app, db
from form import LoginForm, RegistrationForm, TodoListForm
from .model import User, List, load_user

from flask import jsonify, request, redirect, url_for, render_template, flash
from flask_login import current_user, login_user, logout_user, login_required


# @app.route('/')
# def index():
#     # redirect(url_for('login'))
#     return "hello"


@app.route('/login/', methods=['GET', 'POST'])
def login():
    if request.method == 'GET':
        form = LoginForm()
        return render_template('login.html', title='登录', form=form)

    username = request.form['username']
    password = request.form['password']
    if username is None or password is None:
        flash('Invalid')
        return redirect('/login/')

    user = User.query.filter_by(username=username).first()
    if user is None or not user.check_password(password):
        flash('Invalid username or password')
        return redirect('/login/')

    login_user(user)
    flash('login ok')
    return redirect('/')


@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        form = RegistrationForm()
        return render_template('register.html', title='注册', form=form)

    username = request.form['username']
    password = request.form['password']
    if username is None or password is None:
        flash('Invalid')
        return redirect('/register/')

    user = User(username=username, nick_name=username)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    flash('register ok')
    return redirect('/')


@app.route('/logout/')
@login_required
def logout():
    logout_user()
    flash('logout ok')
    return redirect(url_for('login'))


@app.route('/password/reset/', methods=['GET'])
@login_required
def reset_password():
    pass

# d
#


@app.route('/user/<int:id>/', methods=['GET'])
@login_required
def get_user_info(id):
    return


@app.route('/user/<int:id>/', methods=['PUT'])
@login_required
def update_user_info(id):
    pass


# @app.route('/list/', methods=['GET'])
@app.route('/', methods=['GET'])
@login_required
def get_list():
    """
    获取列表，未完成/已完成
    """
    # type = request.query_string('type')
    # if type is None or type != 'todo' and type != 'done':
    #     return redirect('/list/')
    #
    # if type == 'todo':
    #     list = List.query.filter_by(List.status == 0 or List.status == 2).all()
    #     dic = {}
    #     for d in list:
    #
    #     data = jsonify()
    #     return ''

    list = List.query.filter(List.status == 0 or List.status == 2)
    return render_template('list.html', list=list)


@app.route('/list/', methods=['GET', 'POST'])
@login_required
def create_list():
    if request.method == 'GET':
        form = TodoListForm()
        return render_template('todo_list.html', title='todo-list', form=form)

    title = request.form['title']
    content = request.form['content']
    status = request.form['status']
    time = request.form['time']
    user_id = load_user()
    list = List(title=title, content=content, status=status, time=time, user_id=user_id)
    db.session.add(list)
    db.session.commit()
    return redirect('/')


@app.route('/list/<int:id>/', methods=['GET'])
@login_required
def get_list_info(id):
    return


@app.route('/list/<int:id>/', methods=['GET', 'PUT'])
@login_required
def update_list(id):
    if request.method == 'GET':
        todo_list = List.query.filter_by(id=id).first()
        form = TodoListForm(
            title=todo_list.title,
            content=todo_list.content,
            status=todo_list.status,
            time=todo_list.time
        )
        # form.title.data = todo_list.title
        # form.content.data = todo_list.content
        # form.status.data = todo_list.status
        # form.time.data = todo_list.time
        return render_template('todo_list.html', title='todo-list', form=form)

    todo_list = List.query.filter_by(id=id).first()
    todo_list.title = request.form['title']
    todo_list.content = request.form['content']
    todo_list.status = request.form['status']
    todo_list.time = request.form['time']
    db.session.commit()
    flash('update the todo list')
    return redirect('/')


@app.route('/list/<int:id>/', methods=['DELETE'])
@login_required
def delete_list(id):
    todo_list = List.query.filter_by(id=id).first()
    db.session.delete(todo_list)
    db.session.commit()
    flash('delete the todo list')
    return redirect('/')
