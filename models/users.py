from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
	password_hash = db.Column(db.String(128))

	def __init__(self, *args, **kwargs):
		""" Initializes the user """
		super().__init__(*args, **kwargs)

	@property
	def password(self):
		raise AttributeError('passwor is not a readable attribute')

	@password.setter
	def password(self, password):
		self.password_hash = generate_password_hash(password)

	def verify_password(self, password):
		return check_password_hash(self.password_hash, password)