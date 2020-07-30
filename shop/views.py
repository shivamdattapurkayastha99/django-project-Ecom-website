from django.shortcuts import render
from django.http import HttpResponse
from .models import product,contact,orders,OrderUpdate
from math import ceil
import logging
import json
# from django.views.decorators.csrf import csrf_exempt

# import Checksum.py
# MERCHANT_KEY = ''

# Get an instance of a logger
logger = logging.getLogger(__name__)
# Create your views here.
def index(request):
    # products=product.objects.all()
    # print(products)
    
    # n=len(products)
    # nslides=n//4+ceil((n/4)-(n//4))
    # params={'noofslides':nslides,'range':range(nslides),'product':products}
    # allprods=[[products,range(1,nslides),nslides],[products,range(1,nslides),nslides]]
    allprods=[]
    catprods=product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prod=product.objects.filter(category=cat)
        n=len(prod)
        nslides=n//4+ceil((n/4)-(n//4))
        allprods.append([prod,range(1,nslides),nslides])
    params={'allprods':allprods}
    return render(request,'shop/index.html',params)
def about(request):
    
    return render(request,'shop/about.html')
def contact1(request):
    if request.method=="POST":
        
        name=request.POST.get('name','')
        phone=request.POST.get('phone','')
        email=request.POST.get('email','')
        password=request.POST.get('password','')
        
        print(name,phone,email,password)
        contact2=contact(name=name,phone=phone,email=email,password=password)
        contact2.save()
    return render(request,'shop/contact.html')
def tracker(request):
    if request.method=="POST":
        
        OrderId=request.POST.get('OrderId','')
        email=request.POST.get('email','')
        try:
            order=orders.objects.filter(order_id=OrderId,email=email)
            if len(order)>0:
                update=OrderUpdate.objects.filter(order_id=OrderId)
                updates=[]
                for item in update:
                    updates.append({'text':item.update_desc,'time':item.timestamp})
                    response=json.dumps({"status":"success","updates":updates,"itemsJson":order[0].items_json},default=str)
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}')
        except Exception as e:
            return HttpResponse('{"status":"error"}')
    
    return render(request,'shop/tracker.html')
def searchMatch(query,item):
    if query in item.product_name.lower() or query in item.desc.lower() or query in item.category.lower():
        return True
    else:
       return False
def search(request):
    query=request.GET.get('search')
    allprods=[]
    catprods=product.objects.values('category','id')
    cats={item['category'] for item in catprods}
    for cat in cats:
        prodtemp=product.objects.filter(category=cat)
        prod=[item for item in prodtemp if searchMatch(query,item)]

        n=len(prod)
        nslides=n//4+ceil((n/4)-(n//4))
        if len(prod)!=0:
            allprods.append([prod,range(1,nslides),nslides])
    params={'allprods':allprods,'msg':""}
    if len(allprods)==0 or len(query)<4:
        params={'allprods':allprods,'msg':"Please make sure to enter proper search query"}

    return render(request,'shop/index.html',params)
    
    # return render(request,'shop/search.html')
def products(request, myid):
    # Fetch the product using the id
    product1 = product.objects.filter(id=myid)


    return render(request, 'shop/products.html', {'product':product1[0]})
    
def checkout(request):
    if request.method=="POST":
        items_json=request.POST.get('itemsJson','')
        name=request.POST.get('name','')
        amount=request.POST.get('amount','')
        phone=request.POST.get('phone','')
        email=request.POST.get('email','')
        address=request.POST.get('address','')
        city=request.POST.get('city','')
        state=request.POST.get('state','')
        zip_code=request.POST.get('zip_code','')

        
        
        order=orders(items_json=items_json,name=name,amount=amount,phone=phone,email=email,address=address,city=city,state=state,zip_code=zip_code)
        order.save()
        update=OrderUpdate(order_id=order.order_id,update_desc="Order has been placed")
        update.save()
        thank=True
        id=order.order_id
        return render(request,'shop/checkout.html',{'thank':thank,'id':id})
        # param_dict={
        #     'MID':'WorldP64425807474247',
        #     'ORDER_ID':str(order.order_id),
        #     'TXN_AMOUNT':str(amount),
        #     'CUST_ID':'email',
        #     'INDUSTRY_TYPE_ID':'Retail',
        #     'WEBSITE':'WEBSTAGING',
        #     'CHANNEL_ID':'WEB',
	    # 'CALLBACK_URL':'http://127.0.0.1:8000/shop/handlerequest/',
        # }
        # param_dict['CHECKSUMHASH']=Checksum.generate_checksum(param_dict,MERCHANT_KEY)
        # return render(request,'paytm.html',{'param_dict':param_dict})
    return render(request,'shop/checkout.html')
# @csrf_exempt
# def handlerequest(request):
#     form=request.POST
#     response_dict={}
#     for i in form.keys():
#         response_dict[i]=form[i]
#         if i=='CHECKSUMHASH':
#             checksum=form[i]
#     verify=Checksum.verify_checksum(response_dict,MERCHANT_KEY,checksum)
#     if verify:
#         if response_dict['RESPCODE']=='01':
#             print("order successful")
#         else:
#             print("not successful"+response_dict['RESPMSG'])
#     return render(request,'paymentstatus.html',{'response':response_dict})


    
    

