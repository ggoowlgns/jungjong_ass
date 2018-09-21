from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from .models import Product
import MySQLdb


# Create your views here.

aws_ip = "127.0.0.1"

def index(request):
    product = Product.objects.all() #해당 table의 모든 정보를 가져옴
    # no1 = Members.objects.filter(party_number = 1) #select party_number 한것만 가져옴
    str = ''
    for pro in product:
        str += pro


    #############context만들어서 html로 보내기########
    context = {'product': product}


    return render(request, 'jungjong/index.html',context)
