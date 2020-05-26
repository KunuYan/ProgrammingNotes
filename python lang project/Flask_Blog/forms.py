from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, EqualTo, Email
import email_validator

# we are creating the registration for signing up
class RegistrationForm(FlaskForm):
    # each of the fields(username, password, email, etc)

    # The username field, we use validators to make sure that this field is not empty, and min and max username length
    username = StringField('Username', 
                            validators=[DataRequired(), Length(min=6, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                            validators=[DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                            validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')


# now we are creating our login form
class LoginForm(FlaskForm):
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password',
                            validators=[DataRequired()])
    remember = BooleanField('Remember Me')
    submit = SubmitField('Login')