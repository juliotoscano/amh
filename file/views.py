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

def readXSD(request):
    #carregar arquivos xml ou xsd
    tree = ET.parse('nome_arquivo')
    root = tree.getroot()
    #Raiz começa no primeiro element de fato: Ex: mensagemTISS
    root = root.find('{http://www.w3.org/2001/XMLSchema}element')
    if root[0].tag == "{http://www.w3.org/2001/XMLSchema}complexType":
        #Elementos dentro desse no relacionamento direto com o no acima.
        complexType = root[0]
        sequence = complexType[0]
        for x in root.findall('{http://www.w3.org/2001/XMLSchema}element'): 
            print(x.attrib)
    else:
        pass