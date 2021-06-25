from django import forms
from .models import Image,User,Teacher

class ImageForm(forms.ModelForm):
	class Meta:
		model = Image
		fields ='__all__'
		labels = {'photo':''} 


class StudentForm(forms.ModelForm):
	class Meta:
		model = User
		fields = ['name','email','clas','city']


class TeacherForm(forms.ModelForm):
	class Meta:
		model = Teacher
		fields = ['name','email','qly','exp','city','filepath']