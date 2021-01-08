from django.db import models

# Create your models here.
class Expendeture(models.Model):
	title = models.CharField(max_length = 100)
	description = models.TextField(max_length = 250)
	SPChoice = 'SP'
	OOPChoice = 'OOP'
	typeChoices = [(SPChoice, 'Scheduled Payment'), (OOPChoice, 'One-Off Payment')]
	expendetureType = models.CharField(
		max_length = 3,
		choices = typeChoices,
		default = OOPChoice)

	cost = models.DecimalField(decimal_places = 2, max_digits = 10000)
