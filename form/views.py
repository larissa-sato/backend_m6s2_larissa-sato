from django.http import HttpResponseRedirect
from django.shortcuts import render
from .forms import UploadForm
from rest_framework.decorators import APIView


def handler_upload(el):
    with open('challenge_backend-s2/cnab.txt', 'wb+') as destination:
        for chunk in el.chunks():
            destination.write(chunk)

class UploadView(APIView):
    def upload(req):
        if req.method == 'POST':
            form = UploadForm(req.POST, req.FILES)
            if form.is_valid():
                handler_upload(req.FILES['file'])
                return HttpResponseRedirect('/success/url/')
        else:
            form = UploadForm()
        return render(req, 'upload.html', {'form': form})