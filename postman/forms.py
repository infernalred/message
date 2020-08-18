from django import forms

from postman.models import Postman


class PostmanForm(forms.ModelForm):
    class Meta:
        model = Postman
        fields = ("email", "text")
