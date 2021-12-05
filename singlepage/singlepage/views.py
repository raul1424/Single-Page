from django.shortcuts import render
from singlepage.models import employee

def empl(request):
    if request.method=="POST":
        if request.POST.get('firstname') and request.POST.get('lastname') and request.POST.get('email'):
            saveobj=employee()
            saveobj.firstname=request.POST.get('firstname')
            saveobj.lastname=request.POST.get('lastname')
            saveobj.email=request.POST.get('email')
            saveobj.save()
            
            displayrecords=employee.objects.all()
            return render(request, 'index.html',{"employee":displayrecords})

    else:
         displayrecords=employee.objects.all()
    return render(request, 'index.html',{"employee":displayrecords})