from django.http import HttpResponse,HttpResponseRedirect
from StdDetails.models import Registration
from django.shortcuts import render
def Registrations(request):
    if request.method=='POST':
        fname=request.POST['fname']
        mname=request.POST['mname']
        lname=request.POST['lname']
        mob=request.POST['mob']
        email=request.POST['email']
        query=Registration(fname=fname,mname=mname,lname=lname,mob=mob,email=email)
        query.save()
        url="imageupload?reg={}".format("jj")
        return HttpResponseRedirect(url)
    return render(request,"RegistrationForm.html")
def ImageSign(request):
    REG=""
    try:
        if request.method=='GET':
            REG=request.GET['reg']
    except:
        pass
    return render(request,"photo_and_sign.html",{"REG":REG})
def details(request):
    return render(request,"details.html")