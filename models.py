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

class UserProject(Model):
	username = CharField()
	projectname = CharField()

	class Meta:
		database = DATABASE

	@classmethod
	def create_userproject(cls, username, projectname):
		try:
			cls.create(
				username=username,
				projectname=projectname)
		except IntegrityError:
			raise ValueError("User already exists")

	@classmethod
	def get_userprojects(self, name):
		projects = (UserProject
				.select()
				.where(UserProject.username == name))
		return projects

class Project(Model):
	filename = CharField()
	storenumber = CharField(unique=True)
	date = CharField()
	equipment = CharField()
	revisit = CharField()
	fitfortrade = CharField()
	permit = CharField()
	dressed = CharField()
	disruption = CharField()
	contacted = CharField()
	wgll = CharField()
	workplan = CharField()
	complete = CharField()
	champion = CharField()
	spares = CharField()
	trails = CharField()
	managername = CharField()
	position = CharField()
	trafficlight = CharField()

	class Meta:
		database = DATABASE

	@classmethod
	def create_project(cls, filename, storenumber, date, equipment, revisit,
						fitfortrade, permit, dressed, disruption, contacted,
						wgll, workplan, complete, champion, spares, trails,
						managername, position, trafficlight):
		try:
			cls.create(
				filename = filename
				storenumber = storenumber
				date = date
				equipment = equipment
				revisit = revisit
				fitfortrade = fitfortrade
				permit = permit
				dressed = dressed
				disruption = disruption
				contacted = contacted
				wgll = wgll
				workplan = workplan
				complete = complete
				champion = champion
				spares = spares
				trails = trails
				managername = managername
				position = position
				trafficlight = trafficlight
		except IntegrityError:
			raise ValueError("Store info already recieved")

		@classmethod
		def get_project(self):
			projectinfo = (Project
					.select()
					)
			return projectinfo

def initialize():
	DATABASE.connect()
	DATABASE.create_tables([User, UserProject, Project], safe=True)
	DATABASE.close()
