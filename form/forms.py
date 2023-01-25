from django import forms
#from .models import ModelUpload

class UploadForm(forms.Form):
    title = forms.CharField(max_length=50)
    file = forms.FileField()
