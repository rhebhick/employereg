from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.db.models import Q
import datetime
from django.contrib import messages
# Create your views here.
def index(request):
    return render(request,'index.html')

@login_required(login_url='/')
def adminHome(request):
    return render(request,'adminHome.html')

@login_required(login_url='/')
def addD(request) :
    # context={}
    data=Department.objects.all()
    if request.POST :
        dept=request.POST.get('dept')
        re=Department.objects.create(department=dept)
        re.save()
        # context={'dept': dept}
        return redirect('/department')
    return render(request,'addD.html',{'data':data})
# def viewE(request):
#     data=Department.objects.all()
    
#     if request.POST :
#         name=request.POST.get('name')
#         email=request.POST.get('email')
#         age=request.POST.get('age')
#         address=request.POST.get('address')
#         phn=request.POST.get('phn')
#         d_id=request.POST.get('department')
#         department=Department.objects.get(id=d_id)
#         ra=Employees.objects.create(name=name,email=email,age=age,address=address,phn=phn,department=department)
#         ra.save()
#     data2=Employees.objects.all()
#     return render(request,'viewE.html',{'data':data,'data2':data2})

@login_required(login_url='/')
def employe(request):
    data=Department.objects.all()
    message=''
    if request.POST :
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        address=request.POST.get('address')
        phn=request.POST.get('phn')
        d_id=request.POST.get('department')
        password=request.POST.get('password')
        department=Department.objects.get(id=d_id)
        if User.objects.filter(username=email).exists():
            message='this user already exist'
        else :
            re=User.objects.create_user(first_name=name,username=email,password=password,is_staff=1)
            re.save()
            ra=Employees.objects.create(name=name,email=email,age=age,address=address,phn=phn,department=department,password=password,to_user=re)
            ra.save()
            return redirect('/viewEmp')
    data2=Employees.objects.all()
    return render(request,'employe.html',{'data':data,'data2':data2,'message':message})

@login_required(login_url='/')
def delete(request):
    id=request.GET['id']
    data=Department.objects.get(id=id)
    data.delete()
    return redirect('/department')

@login_required(login_url='/')
def delete2(request):
    id=request.GET['id']
    data=Employees.objects.get(id=id)
    a=data.email
    data2=User.objects.get(username=a)
    data2.delete()
    data.delete()
    return redirect('/viewEmp')

@login_required(login_url='/')
def edit1(request):
    id=request.GET['id']
    data=Department.objects.get(id=id)
    if request.POST :
        dept=request.POST.get('dept')
        if dept !='' :
            data.department=dept
            data.save()
            return redirect('/department')
    return render(request,'edit1.html',{'data':data})

@login_required(login_url='/')
def edit2(request):
    id=request.GET['id']
    data=Employees.objects.get(id=id)
    data2=Department.objects.all()
    if request.POST :
        name=request.POST.get('name')
        age=request.POST.get('age')
        email=request.POST.get('email')
        address=request.POST.get('address')
        phn=request.POST.get('phn')
        d_id=request.POST.get("department")
        department=Department.objects.get(id=d_id)
        data.name=name
        data.age=age
        data.email=email
        data.address=address
        data.phn=phn
        data.department=department
        data.save()
        return redirect('/viewEmp')
    return render(request,'edit2.html',{'data':data,'data2':data2})
def customer(request) :
    data=Employees.objects.all()
    message=''
    if request.POST:
        name=request.POST.get('name')
        email=request.POST.get('email')
        age=request.POST.get('age')
        phn=request.POST.get('phn')
        address=request.POST.get('address')
        password=request.POST.get('password')
        e_id=request.POST.get('employe')
        employe=Employees.objects.get(id=e_id)

        if User.objects.filter(username=email).exists():
            message='username taken'
        else:
            ta=User.objects.create_user(username=email, email=email,first_name=name,password=password)
            ta.save()
            te=Customer.objects.create(name=name,email=email,age=age,phn=phn,address=address,password=password,employe=employe,to_user=ta)
            te.save()
    return render(request,'customer.html',{'data':data,'message':message})
def loginP(request):
    message=''
    if request.POST:
        username=request.POST.get('username')
        password=request.POST.get('password')
        # if User.objects.filter(Q(username=username)&Q(password=password)).exists():
        check = authenticate(username=username,password=password)
        if check:
            login(request,check)
            if check.is_superuser:
                return redirect("/adminHome")
            elif check.is_staff:
                data = Employees.objects.get(to_user=check)
                cid = data.id
                request.session['uid'] = cid
                request.session['type']='employe'
                message='login successful'
                return redirect("/empHome")
            else:
                print(check)
                data = Customer.objects.get(to_user=check)
                cid = data.id
                request.session['uid'] = cid
                message='login successful'
                return redirect("/custHome")
        else:
            message='try again'
    return render(request,'login.html',{'msg':message})

@login_required(login_url='/')
def custHome(request):
    uid = request.session['uid']
    user = Customer.objects.get(id=uid)
    return render(request, "custHome.html", {"user":user})

@login_required(login_url='/')
def empHome(request):
    uid = request.session['uid']
    user = Employees.objects.get(id=uid)
    data=Customer.objects.filter(employe=user)
    return render(request, "empHome.html", {"user":user,'data':data})

@login_required(login_url='/')
def cEdit (request):
    id=request.GET['id']
    data=Customer.objects.get(id=id)
    if request.POST:
        name=request.POST.get('name')
        data.name=name
        address=request.POST.get('address')
        data.address=address
        email=request.POST.get('email')
        data.email=email
        age=request.POST.get('age')
        data.age=age
        phn=request.POST.get('phn')
        data.phn=phn
        data.save()
        return redirect('/custHome')
    return render(request,'cEdit.html',{'data':data})

@login_required(login_url='/')
def cDele(request):
    print("============================")
    id=request.GET['id']
    data=User.objects.get(id=id)
    data.delete()
    return redirect('/login')

@login_required(login_url='/')
def done(request) :
        
    return redirect('/login')

@login_required(login_url='/')
def addproduct(request):
    message=''
    if request.POST:
        productName=request.POST.get('pname')
        desc=request.POST.get('desc')
        stock=request.POST.get('stock')
        price=request.POST.get('price')
        img=request.FILES.get('img')
        e_id=request.session['uid']
        e_details=Employees.objects.get(id=e_id)
        if Product.objects.filter(productName=productName).exists() :
            message='this product is already added'
        else :
            ra=Product.objects.create(productName=productName,desc=desc,stock=stock,price=price,img=img,employe=e_details)
            ra.save()
            message='successfully added !'
    return render(request,'addproduct.html',{'message':message})

@login_required(login_url='/')
def viewproduct(request) :
    message=''
    data=Product.objects.all()
    return render(request,'viewproduct.html',{'message':message,'data':data})

@login_required(login_url='/')
def sview(request):
    id=request.GET['id']
    data=Product.objects.get(id=id)
    return render(request,'sview.html',{'data':data})

@login_required(login_url='/')
def buynow(request):
    id=request.GET['id']
    data=Product.objects.get(id=id)
    if Product.objects.filter(id=id).exists() :
        c_id=request.session['uid']
        c_details=Customer.objects.get(id=c_id)
        a=data.stock
        data.stock=a-1
        data.save()
        ra=Purchased.objects.create(product=data,customer=c_details)
        ra.save()
        messages.info(request, "Order Placed")
    return redirect(f'/sview?id={id}')

@login_required(login_url='/')
def history(request):
    c_id=request.session['uid']
    data=Purchased.objects.filter(customer__id=c_id)
    return render(request,'history.html',{'data':data})

@login_required(login_url='/')
def deleteorder(request):
    id=request.GET['id']
    data=Purchased.objects.get(id=id)
    p_id=data.product.id
    data2=Product.objects.get(id=p_id)
    a=data2.stock
    data2.stock=a+1
    data2.save()
    data.delete()
    return redirect('/history')
# def hview(request):
#     id=request.GET['id']
#     data=Purchased.objects.get(id=id)
#     return render(request,'/hview.html',{'data':data})

@login_required(login_url='/')
def purchased_list(request):
    e_id=request.session['uid']
    data=Purchased.objects.filter(product__employe__id=e_id)
    return render(request,'purchased_list.html',{'data':data})

@login_required(login_url='/')
def changeStatus(request):
    status=request.GET['status']
    id=request.GET['id']
    data=Purchased.objects.get(id=id)
    data.status=status
    data.save()
    return redirect('/purchased_list')

@login_required(login_url='/')
def editproduct(request):
    id=request.session['uid']
    data=Product.objects.filter(employe__id=id)
    return render(request,'editproduct.html',{'data':data})

@login_required(login_url='/')
def deleteproduct(request):
    id=request.GET['id']
    data=Product.objects.get(id=id)
    data.delete()
    return redirect('/editproduct')

@login_required(login_url='/')
def ineditproduct(request):
    id=request.GET['id']
    data=Product.objects.get(id=id)
    if request.POST :
        productName=request.POST.get('productName')
        price=request.POST.get('price')
        desc=request.POST.get('desc')
        stock=request.POST.get('stock')
        img=request.FILES.get('img')
        data.price=price
        data.desc=desc
        data.stock=stock
        data.img=img
        data.productName=productName
        data.save()
        return redirect('/editproduct')
    return render(request,'ineditproduct.html',{'data':data})

@login_required(login_url='/')
def department(request):
    data=Department.objects.all()
    return render(request,'department.html',{'data':data})

@login_required(login_url='/')
def viewEmp(request):
    data2=Employees.objects.all()
    return render(request,'viewEmp.html',{'data2':data2})

@login_required(login_url='/')
def yourC(request):
    e_id=request.session['uid']
    data=Customer.objects.filter(employe__id=e_id)
    return render(request,'yourC.html',{'data':data})
@login_required(login_url='/')
def activeS(request):
    id=request.GET['id']
    data2=Customer.objects.get(id=id)
    a=data2.email
    data=User.objects.get(username=a)
    status=request.GET['status']
    data.is_active  = status
    data.save()
    return redirect("/yourC")
def logoutFun(request):
    logout(request)
    request.session.flush()
    return redirect('/')



