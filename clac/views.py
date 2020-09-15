from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def home(request):
    # return HttpResponse("Hello world") #this line was used earlier when we had just retrived 
    #the content from this line but now we need to call the home.html page so we need to use rende function now.
    return render(request,'home.html',{'name':'Pratik'})
def add(request):
    val1=request.POST['num1'] #POST is best to submit data GET is best to retrive data
    val2=request.POST['num2']
    result=int(val1)+int(val2)
    return render(request,"result.html",{'result':result})
def mul(request):
    val1=request.GET['num1'] #GET will display the data on the addres bar which can be low for security reasons so its better to use POSt
    val2=request.GET['num2']
    reult=int(val1)*int(val2)
    return render(request,"result.html",{'result':reult})