import datetime

from flask.ext.bcrypt import generate_password_hash
from flask.ext.login import UserMixin
from peewee import *

DATABASE = SqliteDatabase('signoff.db')

class User(UserMixin, Model):
	username = CharField(unique=True)
	email = CharField(unique=True)
	password = CharField(max_length=100)
	joined_at = DateTimeField(default=datetime.datetime.now)
	is_admin = BooleanField(default=False)
	position = CharField()

	class Meta:
		database = DATABASE

	@classmethod
	def create_user(cls, username, email, password, admin, position):
		try:
			cls.create(
				username=username,
				email=email,
				password=generate_password_hash(password),
				is_admin=admin,
				position=position)
		except IntegrityError:
			raise ValueError("User already exists")

class Project(Model):
	username = CharField()
	projectname = CharField()

	class Meta:
		database = DATABASE

	@classmethod
	def get_projects(self, name):
		projects = (Project
				.select()
				.where(Project.username == name))
		return projects

				# .join(UserProject)
				# .join(User)


	@classmethod
	def create_project(cls, username, projectname):
		try:
			cls.create(
				username=username,
				projectname=projectname)
		except IntegrityError:
			raise ValueError("User already exists")

class UserProject(Model):
	user = ForeignKeyField(User)
	project = ForeignKeyField(Project)

	class Meta:
		database = DATABASE
		indexes = (
			(('user', 'project'), True)
		)

def initialize():
	DATABASE.connect()
	DATABASE.create_tables([User, Project, UserProject], safe=True)
	DATABASE.close()
