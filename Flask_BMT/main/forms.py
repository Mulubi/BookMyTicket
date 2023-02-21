from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo
from Flask_BMT.models.users import User


class RegistrationForm(FlaskForm):

    def validate_last_name(self, last_name_to_check):
        user = User.query.filter_by(last_name=last_name_to_check.data).first()
        if user:
            raise ValidationError("User with that last name already exists! Please try a different last name")

    def validate_email(self, email_to_check):
        email = User.query.filter_by(email=email_to_check.data).first()
        raise ValidationError("Email Address already exists! Please try a different email")

    first_name = StringField(label="First Name", validators=[DataRequired(), Length(min=2, max=20)])
    last_name = StringField(label="Last Name", validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField(label="Email Address", validators=[DataRequired(), Email()])
    password = PasswordField(label="Password", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField(label="Confirm Password", validators=[DataRequired(), EqualTo("Password")])
    submit = SubmitField("Sign Up")


class LoginForm(FlaskForm):
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired()])
    remember = BooleanField("Remember me")
    submit = SubmitField("Login")
