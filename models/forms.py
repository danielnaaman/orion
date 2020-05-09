from flask_wtf import FlaskForm
from wtforms import Form, StringField, SubmitField, TextField, TextAreaField, SelectField, BooleanField, PasswordField, validators#, ValidationError
from wtforms.fields.html5 import DateField
from wtforms.validators import DataRequired, Length

class RegisterFormStructure(FlaskForm):
    firstname = StringField('First Name', validators = [DataRequired()])
    lastname = StringField('Last Name', validators = [DataRequired()])
    username = StringField('Username', validators = [DataRequired(), Length(3)])
    password = PasswordField('Password', validators = [DataRequired(), Length(8)])
    submit = SubmitField('Register')

class LoginFormStructure(FlaskForm):
    username = StringField('Username', validators = [DataRequired(), Length(3)])
    password = PasswordField('Password', validators = [DataRequired(), Length(8)])
    submit = SubmitField('Login')

class QueryFormStructure(FlaskForm):
    state = SelectField('State', validators = [DataRequired()])
    startDate = DateField('Start Date', format='%Y-%m-%d', validators = [DataRequired()])
    endDate = DateField('End Date', format='%Y-%m-%d', validators = [DataRequired()])
    submit = SubmitField('Query')