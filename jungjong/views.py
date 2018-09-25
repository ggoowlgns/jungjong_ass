from django.shortcuts import render
from django.http import HttpResponse,HttpResponseRedirect
from django.views.decorators.csrf import csrf_exempt
from .models import Product_real
import MySQLdb
from furl import furl
import urllib.parse as urlparse

# Create your views here.

aws_ip = "127.0.0.1"

def index(request):
    product = Product_real.objects.all() #해당 table의 모든 정보를 가져옴
    # no1 = Members.objects.filter(party_number = 1) #select party_number 한것만 가져옴
    str = ''
    for pro in product:
        str += "pro_name: {} <br> pro_count : {} ".format(pro.pro_name,pro.pro_count)


    print(str)
    #############context만들어서 html로 보내기########
    context = {'product': product}


    return render(request, 'jungjong/index.html',context)

#put product
@csrf_exempt
def put_product(request):
    connection = MySQLdb.connect(host=aws_ip,
                                 user="pjh",
                                 passwd="root",
                                 db="jungjong_ass",
                                 use_unicode=True,
                                 charset="utf8")
    cursor = connection.cursor()

    if request.method == 'PUT':
        test = "http://test/test?"
        test += request.read().decode('utf-8')
        parsed = urlparse.urlparse(test)
        pro_name = urlparse.parse_qs(parsed.query)['pro_name'][0]
        pro_count = urlparse.parse_qs(parsed.query)['pro_count'][0]
        staff_data = [(str(pro_name),str(pro_count))]
        for p in staff_data:
            format_str = """INSERT INTO jungjong_product_real (pro_name , pro_count )
            VALUES ( "{pro_name}","{pro_count}" );
            """
            sql_command = format_str.format(pro_name=p[0], pro_count=p[1])
            print("inserted")
            cursor.execute(sql_command)

        #####conection 모두 종료########
        connection.commit()
        cursor.close()
        connection.close()

    return HttpResponse("suc")

#put product
@csrf_exempt
def update_product(request):
    connection = MySQLdb.connect(host=aws_ip,
                                 user="pjh",
                                 passwd="root",
                                 db="jungjong_ass",
                                 use_unicode=True,
                                 charset="utf8")
    cursor = connection.cursor()

    if request.method == 'PUT':
        test = "http://test/test?"
        test += request.read().decode('utf-8')
        parsed = urlparse.urlparse(test)
        pro_name = urlparse.parse_qs(parsed.query)['pro_name'][0]
        pro_count = urlparse.parse_qs(parsed.query)['pro_count'][0]
        staff_data = [(str(pro_name),str(pro_count))]
        for p in staff_data:
            format_str = "UPDATE jungjong_product_real set pro_count= \'" + pro_count + "\' WHERE pro_name = \'" + pro_name + "\';"
            sql_command = format_str
            print("updated")
            cursor.execute(sql_command)

        #####conection 모두 종료########
        connection.commit()
        cursor.close()
        connection.close()

    return HttpResponse("suc")


@csrf_exempt
def yun_test(request):
    if request.method == 'PUT':
        test = "http://test/test?"
        test += request.read().decode('utf-8')
        parsed = urlparse.urlparse(test)
        status = urlparse.parse_qs(parsed.query)['status'][0]
        print('status', status)
    return HttpResponse("suc")

