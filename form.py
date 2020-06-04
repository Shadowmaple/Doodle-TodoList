from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, DateTimeField, RadioField
from wtforms.validators import DataRequired, length, EqualTo, ValidationError
from app.model import User


class LoginForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), length(1, 20)])
    password = PasswordField('密码', validators=[DataRequired(), length(1, 20)])
    remember_me = BooleanField('记住我')
    submit = SubmitField('登录')


class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), length(1, 20)])
    nick_name = StringField('Nick_name', validators=[DataRequired(), length(1, 20)])
    password = PasswordField('Password', validators=[DataRequired(), length(1, 20)])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('注册')

    @staticmethod
    def validate_username(username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')


class TodoListForm(FlaskForm):
    title = StringField('标题', validators=[DataRequired(), length(1,20)])
    content = StringField('内容', validators=[length(0, 250)])
    status = RadioField('是否完成', validators=[DataRequired()], choices=[('0', '未完成'), ('1', '已完成')])
    submit = SubmitField('提交')


class UserForm(FlaskForm):
    username = StringField('用户名', validators=[DataRequired(), length(1, 20)])
    nick_name = StringField('昵称', validators=[DataRequired(), length(1, 20)])
    submit = SubmitField('保存')
