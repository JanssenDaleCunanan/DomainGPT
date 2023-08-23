from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse

import json

from search_engine import functions as fn


# Create your views here.
def home(request):
    return render(request,"search_engine/home.html")


async def DomainSearch(request):

    domain=json.dumps([request.GET.get("domain")])
     
    return render(request,"search_engine/DomainSearch.html",{"domain":domain
        })


async def suggestions(request):
    
    domain=request.GET.get("domain")

    data=fn.GenerateSimilar(domain)
    
    data_json=json.dumps(data)

 
    return HttpResponse(data_json)


async def availability(request):
    
    domain=request.GET.get("domain")

    data=fn.GetAvailability(domain)
    
    data_json=json.dumps(data)

 
    return HttpResponse(data_json)