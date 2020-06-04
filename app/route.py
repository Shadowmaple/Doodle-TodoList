from . import app, db
from form import LoginForm, RegistrationForm, TodoListForm, UserForm
from .model import User, List, load_user

from flask import request, redirect, url_for, render_template, flash
from flask_login import current_user, login_user, logout_user, login_required
import datetime

status_dic = {0: '未完成', 1: '已完成'}

""" ---- auth routers --- """

# 登录
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


# 注册
@app.route('/register/', methods=['GET', 'POST'])
def register():
    if request.method == 'GET':
        form = RegistrationForm()
        return render_template('register.html', title='注册', form=form)

    username = request.form['username']
    password = request.form['password']
    nick_name = request.form['nick_name']
    if username is None or password is None or nick_name is None:
        flash('Invalid')
        return redirect('/register/')

    user = User(username=username, nick_name=nick_name)
    user.set_password(password)
    db.session.add(user)
    db.session.commit()
    flash('register ok')
    return redirect('/login')


# 登出
@app.route('/logout/')
@login_required
def logout():
    logout_user()
    flash('logout ok')
    return redirect('/login')


# user routers
""" ---- user routers --- """


# 获取用户信息/用户主页
@app.route('/user/info/', methods=['GET'])
@login_required
def get_user_info():
    user = load_user(current_user.id)
    return render_template('user_profile.html', title='用户信息', user=user)


# 修改用户信息
@app.route('/user/update/', methods=['GET', 'POST'])
@login_required
def update_user_info():
    if request.method == 'GET':
        user = User.query.filter_by(id=current_user.id).first()
        form = UserForm(
            username=user.username,
            nick_name=user.nick_name,
        )
        return render_template('user_update.html', title='用户信息', form=form)

    form = UserForm()
    if form.validate_on_submit():
        user = User.query.filter_by(id=current_user.id).first()
        user.username = form.username.data
        user.nick_name = form.nick_name.data
        db.session.commit()
        flash('update user info')
    return redirect(url_for('get_user_info'))


""" ---- todo-list routers --- """


# 获取todo-list
@app.route('/', methods=['GET'])
@login_required
def get_list():
    form = TodoListForm()
    todo_list = List.query.filter(List.user_id == current_user.id).all()
    list = []
    for t in todo_list:
        list.append({
            'id': t.id,
            'title': t.title,
            'content': t.content,
            'status': status_dic[t.status],
            'time': t.time,
        })
    return render_template('index.html', list=list, form=form)


# 新增todo-list
@app.route('/list/', methods=['GET', 'POST'])
@login_required
def create_list():
    form = TodoListForm()
    if request.method == 'GET':
        return render_template('todo_list.html', form=form)

    if form.validate_on_submit():
        todo_list = List(
            title=form.title.data,
            content=form.content.data,
            status=form.status.data,
            time=datetime.datetime.now(),
            user_id=current_user.id,
        )
        db.session.add(todo_list)
        db.session.commit()
        flash('add a new todo list')
    return redirect('/')


# 修改todo-list
@app.route('/list/<int:id>/update/', methods=['GET', 'POST'])
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
        return render_template('todo_list.html', form=form)

    todo_list = List.query.filter_by(id=id).first()
    todo_list.title = request.form['title']
    todo_list.content = request.form['content']
    todo_list.status = request.form['status']
    db.session.commit()
    flash('update a todo list')
    return redirect('/')


# 删除todo-list
@app.route('/list/<int:id>/delete/')
@login_required
def delete_list(id):
    todo_list = List.query.filter_by(id=id).first()
    db.session.delete(todo_list)
    db.session.commit()
    flash('delete a todo list')
    return redirect('/')
