from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


# Create your forms here.
class NewUserForm(UserCreationForm):
	first_name = forms.CharField()

	class Meta:
		model = User
		fields = ("first_name", "username", "password1", "password2")

	def save(self, commit=True):
		user = super(NewUserForm, self).save(commit=False)
		user.first_name = self.cleaned_data['first_name']
		if commit:
			user.save()
		return user

