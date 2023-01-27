from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadForm
from .services import handle_uploaded


def home_form(req):
    if req.method == 'GET':
        form = UploadForm()
        return render(req, 'model_form.html', {'form': form})
    else:
        form = UploadForm(req.POST, req.FILES)
        if form.is_valid():
            handle_uploaded(req.FILES['file'])
            form = UploadForm()
            return render(req, 'model_form.html', {'form': form})  