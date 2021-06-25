from django.db import models
from .validators import validate_file_size
from django.core.validators import FileExtensionValidator

# Create your models here.
class Image(models.Model):
	
	photo = models.ImageField(upload_to = 'pics')
	name = models.CharField(max_length=50,null=True,blank=True)

	def __str__(self):
		return self.name


# Create your models here.
class User(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField(max_length=40)
	clas = models.CharField(max_length=30)
	city = models.CharField(max_length=40)
	
class Teacher(models.Model):
	name = models.CharField(max_length=30)
	email = models.EmailField(max_length=40)
	qly = models.CharField(max_length=30)
	exp = models.CharField(max_length=40)
	city = models.CharField(max_length=40)
	filepath= models.FileField(upload_to='', verbose_name="", validators=[validate_file_size,FileExtensionValidator(allowed_extensions=['.doc','pdf','.docx'])])

	def __str__(self):
		return self.name + ": " + str(self.filepath)

	