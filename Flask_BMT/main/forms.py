from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from Flask_BMT.models.users import User


class RegistrationForm(FlaskForm):
    first_name = StringField(label="First Name", validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField(label="Last Name", validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField(label="Email Address", validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField(label="Confirm Password", validators=[DataRequired(), EqualTo("Password", message='Passwords must match.')])
    submit = SubmitField("Sign Up")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_last_name(self, field):
        if User.query.filter_by(last_name=field.data).first():
            raise ValidationError('Username with that last name already exists.')




class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Length(1, 64), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField("Login")
