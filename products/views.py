from django.http import HttpResponse
from django.shortcuts import render
import json
from . import filter
resultList=[]
product_len=0
# Create your views here.
def index(request):
    return render(request,"products/index.html")

def params(request,param):
    pass

def name(request):
    filter_options=filter.option_set()
    print(filter_options)
    return render(request,"products/name.html",filter_options)

def filterSelect(request):
    global resultList,product_len
    resultList=[]
    data=json.loads(request.GET["data"])
    #print(filter.filter(Company=data["Company"]))
    resultList=filter.filter(Company=data["Company"], Cpu=data["Cpu"], OpSys=data["OpSys"], TypeName=data["TypeName"],Ram=data["Ram"], Price=data["Price"],MemSize=data["MemorySize"],MemType=data["MemoryType"])
    product_len=len(resultList)
    return render(request,"products/productDisplay.html",{"Result":resultList[0:10],"page":1})

def nextPage(request):
    #print(product_len)
    nextvisible="visible"
    pageno=int(request.GET["pageno"])
    return render(request,"products/productDisplay.html",{"Result":resultList[(((pageno-1)*10)):(((pageno-1)*10)+10)],"page":(pageno)})
    
def previousPage(request):
    pageno=int(request.GET["pageno"])
    return render(request,"products/productDisplay.html",{"Result":resultList[(((pageno-2)*10)):(((pageno-2)*10)+10)],"page":(pageno-1)})