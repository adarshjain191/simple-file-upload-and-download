from django.shortcuts import render
#newly added
from django.contrib.auth.models import User,auth
from .models import upload
# Create your views here.

def index(request):
    return render(request,'index.html')
def index1(request):
    if request.method=='POST':
        title=request.POST['title']       
        upload1=request.FILES['upload']
        object=upload.objects.create(title=title,upload=upload1)
        object.save()  
    context=upload.objects.all()
    return render(request,'index1.html',{'context':context})

