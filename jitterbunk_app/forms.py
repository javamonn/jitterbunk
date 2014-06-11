from django import forms


class BunkSomeone(forms.Form):
    user_to_bunk = forms.CharField()
