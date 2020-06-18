from django.shortcuts import render
from django.db import models
from django.db import connection
# Create your views here.
def index(request):
    return render(request,"index.html")
def admin(request):
        id=request.POST["name"]
        pword=request.POST["pword"]
        return render(request,"admin.html",{'name':id,'pword':pword})
def super_admin(request):
    id=request.POST["name"]
    pword=request.POST["pword"]
    if (id in "100") &( pword in "cbit"): #static userid,password
        return render(request,"super_admin.html")
    else:
        return render(request,"index.html")
