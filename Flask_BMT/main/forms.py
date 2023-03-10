from flask_wtf import FlaskForm
from wtforms import DateTimeField, StringField, PasswordField, SubmitField, BooleanField, ValidationError
from wtforms.validators import DataRequired, Length, Email, EqualTo
from Flask_BMT.models.users import User


class RegistrationForm(FlaskForm):
    first_name = StringField(label="First Name", validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField(label="Last Name", validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField(label="Email Address", validators=[DataRequired(), Length(1, 64), Email()])
    password_hash = PasswordField(label="Password", validators=[DataRequired(), Length(min=8), EqualTo("confirm_password",  message='Passwords must match.')])
    confirm_password = PasswordField(label="Confirm Password", validators=[DataRequired()])
    submit = SubmitField("Sign Up")

    def validate_email(self, field):
        if User.query.filter_by(email=field.data).first():
            raise ValidationError('Email already registered.')

    def validate_last_name(self, field):
        if User.query.filter_by(last_name=field.data).first():
            raise ValidationError('Username with that last name already exists.')




class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Length(1, 64), Email()])
    password_hash = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class PasswordForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Length(1, 64), Email()])
    password_hash = PasswordField("Password", validators=[DataRequired()])
    submit = SubmitField("Login")


class TheatreForm(FlaskForm):
    procedure_time = DateTimeField(validators=[DataRequired()])
    patient_name = StringField("Name of patient", validators=[DataRequired()])
    procedure_name = StringField("Procedure", validators=[DataRequired()])
    surgeon = StringField("Surgeon", validators=[DataRequired()])
    anaesthetist = StringField("Anaesthetist", validators=[DataRequired()])
    submit = SubmitField("Create Booking")

class TheatreAddForm(FlaskForm):
    procedure_time = DateTimeField("Time", validators=[DataRequired()])
    patient_name = StringField("Patient", validators=[DataRequired()])
    procedure_name = StringField("Procedure", validators=[DataRequired()])
    surgeon = StringField("Surgeon", validators=[DataRequired()])
    anaesthetist = StringField("Anaesthetist", validators=[DataRequired()])
    submit = SubmitField("Create Booking")

class DashboardForm(FlaskForm):
    pass