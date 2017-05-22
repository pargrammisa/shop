from django import forms
class FirstForm(forms.Form):
	your_name=forms.CharField(max_length=100)
	test=forms.CharField(max_length=100)