from django.db import models

# Create your models here.

# Questions in database
class Question(models.Model):
	question_text = models.CharField(max_length = 5000)
	choice = models.ForeignKey(Choices)
	# all choices are numbered 1 - 10 at most in the database
	correct_choice = models.IntegerField()
	user_choice = models.IntegerField()
	
# question choices
class Choices(models.Model):
	choice_text = models.CharField(max_length = 200)

# user profile
class User(models.Model):
	name = models.charField(max_length = 20)
	password = models.CharField(widget = PasswordInput)
	question = models.ForeignKey(Question)