from django.shortcuts import render
from django.http import HttpResponse


# Get an instance of a logger

# Create your views here.
def index(request):
    # products=product.objects.all()
    # print(products)
    
    # n=len(products)
    # nslides=n//4+ceil((n/4)-(n//4))
    # params={'noofslides':nslides,'range':range(nslides),'product':products}
    # allprods=[[products,range(1,nslides),nslides],[products,range(1,nslides),nslides]]
    
    return render(request,'index.html')