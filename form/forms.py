from django import forms
#from .models import ModelUpload

class UploadForm(forms.Form):
    file = forms.FileField(required=True, error_messages={'invalid':'Erro ao carregar o arquivo'})
