from django import forms


class Studentregister(forms.Form):
    name = forms.CharField()
    email = forms.CharField()
    password = forms.CharField()
    comment = forms.CharField()


