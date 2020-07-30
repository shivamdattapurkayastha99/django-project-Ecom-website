from django.shortcuts import render

# Create your views here.

from django.http import HttpResponse
from .models import Blogpost

# Create your views here.
def index(request):
    # return HttpResponse("Index blog")
    myposts=Blogpost.objects.all()
    print(myposts)
    return render(request,'blog/index.html',{'myposts':myposts})
def blogpost(request,id):
    # return HttpResponse("Index blog")
    post=Blogpost.objects.filter(post_id=id)[0]
    print(post)
    return render(request,'blog/blogpost.html',{'post':post})


