from django import forms
class contactform (forms.Form):
	fullname=forms.CharField()
	email=forms.EmailField()
	contet=forms.CharField(widget=forms.Textarea)