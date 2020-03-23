from django.shortcuts import render
from django.http import HttpResponseRedirect

from .forms import UploadFileForm
from .models import File

# Create your views here.
def upload_file(request):
    if 'type' in request.session and request.session['type'] in settings.ALLOWED_USERS:
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            inst = File(name=request.POST['title'] , payload=request.FILES['file'])
            inst.save()
            return HttpResponseRedirect('/upload/success')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form':form})