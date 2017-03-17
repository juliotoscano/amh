from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .forms import updateXML
from django.urls import reverse

# Create your views here.
def upload_file(request):
    if request.method == 'POST':
        form = updateXML(request.POST,request.FILES)
        if form.is_valid():
            return HttpResponseRedirect(reverse('core:index'))
        else:
            pass
    else:
        form = updateXML()
    return render(request,'create_file.html',{'form':form})