from django.db import models

from django import forms

class UploadForm(forms.Form):
    file = forms.FileField()


