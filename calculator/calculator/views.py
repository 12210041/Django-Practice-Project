from django.http import HttpResponse
from django.shortcuts import render
def hello(request):
    reg="bbb"
    try:  
        if request.method=="GET":
            if int(request.GET['a'])%2!=0:
                reg="False"
            else:
                reg="True"
    except:
        pass
    return render(request,"index.html",{"reg":reg})
    