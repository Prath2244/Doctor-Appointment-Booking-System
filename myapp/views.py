from django.shortcuts import render,redirect
from .models import Userinfo,Doctorinfo,Register
from django.contrib import messages

# Create your views here.

def index(request):
    return render(request,'index.html')

def signup(request):
    if request.method=="POST":
        e_mail=request.POST.get('mail')
        u_pas=request.POST.get('code')
        u_c_pass=request.POST.get('c_pass')
        user=Userinfo.objects.filter(email=e_mail)
        if user.exists():
            messages.error(request,"user already exist")
        elif u_pas != u_c_pass:
            messages.error(request,"password not match")
        else:
            Userinfo.objects.create(email=e_mail,pssword=u_pas)
        return render(request,'login.html')
        
    return render(request,'signup.html')

def login(request):
    if request.method=="POST":
        e_mail=request.POST.get('mail')
        u_pas=request.POST.get('code')
        user=Userinfo.objects.filter(email=e_mail,pssword=u_pas)
        if user.exists():
            return redirect('/home/')
        else:
            messages.error(request,"incorrect password or email")
    return render(request,'login.html')

def home(request):
    docts=Doctorinfo.objects.all()
    return render(request,'home.html',{'doctors':docts})

def register(request):
    if request.method=="POST":
        d_name=request.POST.get('you')
        p_name=request.POST.get('me')
        date=request.POST.get('date')
        pro=request.POST.get('reason')
        Register.objects.create(d_name=d_name,p_name=p_name,name=date,reason=pro)
        return render(request,'succes.html')
    return render(request,'register.html')

def form(request,id):
    doctor=Doctorinfo.objects.get(id=id)
    return render(request,'register.html',{'docto':doctor})