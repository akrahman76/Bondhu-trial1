from django import forms

class CreateNewProfile(forms.Form):
    name = forms.CharField(label="Name", max_length=200)
    gender = forms.CharField(label="Gender", max_length=100)
    date_of_birth = forms.DateField(label="DOB")

