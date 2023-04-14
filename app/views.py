from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
from app.models import *

def insert_topic(request):
    if request.method=='POST':
        tn=request.POST['tn']
        TO=Topic.objects.get_or_create(tname=tn)[0]
        TO.save()
        return HttpResponse('Topic date the insert successfully')

    return render(request,'insert_topic.html')


def insert_webpages(request):
    if request.method=='POST':
        tn=request.POST['topic']
        TO=Topic.objects.get(tname=tn)
        
        
        n=request.POST['n']
        E=request.POST['E']
        u=request.POST['u']
        WO=Webpages.objects.get_or_create(tname=TO,name=n, Email=E, url=u)[0]
        WO.save()
        return HttpResponse('webpage inserted sucessfully')
    LOW=Topic.objects.all()
    d={'topic':LOW}
    return render(request,'insert_webpages.html',d)


