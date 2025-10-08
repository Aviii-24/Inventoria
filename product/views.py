from django.shortcuts import render,redirect
from .models import ProductList
from django.contrib.auth import login,logout,authenticate
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.db.models import Q

# Create your views here.

def home(request):
    return render(request,"home.html",)

@login_required
def show(request):
    obj = ProductList.objects.all()
    context = {
        'prod':obj
    }
    return render(request,"show.html",context)

@login_required
def add(request):
    if request.method=="POST":
        pid = request.POST.get("pid")
        pname =request.POST.get("pname")
        price =request.POST.get("price")
        description =request.POST.get("description")
        category =request.POST.get("category")
        pimage = request.FILES.get("pimage")
        obj = ProductList(pid,pname,category,price,pimage,description)
        obj.save()
        return redirect("show")
    return render(request,"add.html")

def delete(request,pid):
    obj = ProductList.objects.get(pid=pid)
    obj.delete()
    return redirect("show")

def edit(request,pid):
    obj = ProductList.objects.get(pid=pid)
    context = {
        'obj':obj
    }
    if request.method=="POST":
        pname = request.POST.get("pname")
        price = request.POST.get("price")
        description = request.POST.get("description")
        category = request.POST.get("category")
        pimage = request.POST.get("pimage")

        obj.pname = pname
        obj.price = price
        obj.description = description
        obj.category = category
        obj.pimage = pimage
        obj.save()
        return redirect('show')
    
    return render(request,'edit.html',context)

@login_required
def search_products(request):
    query = request.GET.get("q") #'q' is the input name from the form
    results = ProductList.objects.all()
    if query:
        #results = results.filter(pname__icontains=query) # search in product name
        #you can also search in description:
        results = results.filter(Q(pname__icontains=query)| Q(description__icontains=query))
    return render(request,'search_products.html',{'results':results,'query':query})

def loginu(request):
    if request.method =="POST":
        uname = request.POST.get("username")
        password = request.POST.get("password")
        try:
            user = User.objects.get(username=uname)
        except User.DoesNotExist:
            return render(request,"login.html",{'error':"User Not Found...Please Try Again"})
        #if both username and password are valid 
        user = authenticate(request,username = uname,password=password)
        if user is not None:
            login(request,user)
            return redirect("show")
    return render(request,"login.html",{})

def register(request):
    if request.method =="POST":
        uname = request.POST.get("username")
        email = request.POST.get("email")
        password = request.POST.get("password")
        if User.objects.filter(username=uname).exists():
            return render(request,"register.html",{"error":"User is Already Exists"})
        else:
            User.objects.create_user(username = uname,email = email,password = password)
            return redirect("loginu")
    return render(request,"register.html",{})

def logoutu(request):
    logout(request)
    return redirect("loginu")

@login_required
def electronics(request):
    obj = ProductList.objects.filter(category = "Electronics")
    context ={
        "obj":obj
    }
    if obj.exists():
        return render(request,"electronics.html",context)
    else:
        return render(request,"home.html",{"error" : "Currently the Products of that Category are Out of Stock...."})
    
@login_required
def carandmotorbikes(request):
    obj = ProductList.objects.filter(category="Cars and Motorbikes")
    context ={
        "obj":obj
    }
    if obj.exists():
        return render(request,"carandmotorbikes.html",context)
    else:
        return render(request,"home.html",{"error":"Currently the Products of that Category are Out of Stock"})
    
@login_required
def homeandkitchen(request):
    obj = ProductList.objects.filter(category="Home and Kitchen")
    context ={
        "obj":obj
    }
    if obj.exists():
        return render(request,"homeandkitchen.html",context)
    else:
        return render(request,"home.html",{"error":"Currently the Products of that Category are Out of Stock"})
    
def fashion(request):
    obj = ProductList.objects.filter(category="Fashion")
    context ={
        "obj":obj
    }
    if obj.exists():
        return render(request,"fashion.html",context)
    else:
        return render(request,"home.html",{"error":"Currently the Products of that Category are Out of Stock"})