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


def insert_accessrecord(request):
    if request.method=='POST':
        n=request.POST['topic']
        WO=Webpages.objects.get(name=n)
        WO.save()
          
        d=request.POST['d']
        a=request.POST['a']
        AO=AccessRecord.objects.get_or_create(name=WO, author=a,date=d)[0]
        AO.save()
        return HttpResponse('accessrecord inserted in successfully')

    LOA=Webpages.objects.all()
    d={'topic':LOA}
    return render(request,'insert_accessrecord.html',d)



