from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import updateXML
from django.urls import reverse
from .ElementTree import ElementTree as ET
from django.core.files.uploadedfile import UploadedFile
#from django.core.files import File

# Create your views here.
def upload_file(request):
    if request.method == 'POST':
        form = updateXML(request.POST,request.FILES)
        if form.is_valid():
            listfiles = request.FILES.getlist("lot")
            for x in listfiles:
                filetemp = updateXML(x)
                tree = ET.parse(filetemp)
                root = tree.getroot()
            return HttpResponseRedirect(reverse('core:index'))
        else:
            pass
    else:
        form = updateXML()
    return render(request,'create_file.html',{'form':form})