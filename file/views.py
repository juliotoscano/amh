from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import updateXML
from django.urls import reverse
from .ElementTree import ElementTree as ET
from django.core.files.uploadedfile import UploadedFile
import os
uploadfiles = os.path.dirname(__file__)
#from django.core.files import File

# Create your views here.
def upload_file(request):
    if request.method == 'POST':
        listfiles = request.FILES.getlist("lot")
        for count, x in enumerate(listfiles):
            def process(f):
                file_path = os.path.join(uploadfiles,'upload','file_'+ str(count)+'.xml')
                with open(file_path,'wb+') as destination:
                    for chunk in f.chunks():
                        destination.write(chunk)
            process(x)
        return HttpResponse("Files Uploaded!")
        #form = updateXML(request.POST,request.FILES)
        #if form.is_valid():
        #   listfiles = request.FILES.getlist("lot")
        #  for x in listfiles:
        #       filetemp = updateXML(x)
        #       tree = ET.parse(filetemp)
        #       root = tree.getroot()
        #  return HttpResponseRedirect(reverse('core:index'))
    else:
        form = updateXML()
    return render(request,'uploadXml.html',{'form':form})