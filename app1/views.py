from django.shortcuts import render,HttpResponse,HttpResponseRedirect
from . forms import PatientRegistraion
from . models import User1,User2
from django.contrib.auth.models import Group
from .forms import SignUpForm, LoginForm
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout

# Create your views here.
def index(request):
    return render(request,"index.html")

def about(request):
  return render (request,"about.html")

def contact(request):
    if request.method=="POST":
        nm=request.POST["name"]
        ph=request.POST["Phone"]
        em=request.POST["email"]
        sb=request.POST["subject"]
        ms=request.POST["Message"]
        us2=User2(name=nm,Phonenumber=ph,email=em,subject=sb,message=ms)
        us2.save()
    else:
        print ("Something went wrong")    
    return render(request,"contact.html")

def user_login(request):
 if not request.user.is_authenticated:
  if request.method == "POST":
   form = LoginForm(request=request, data=request.POST)
   if form.is_valid():
    uname = form.cleaned_data['username']
    upass = form.cleaned_data['password']
    user = authenticate(username=uname, password=upass)
    if user is not None:
     login(request, user)
     messages.success(request, 'Logged in Successfully !!')
     return HttpResponseRedirect('/add/')
  else:
   form = LoginForm()
  return render(request, 'login.html', {'form':form})
 else:
  return HttpResponseRedirect('/')


def user_logout(request):
 logout(request)
 return HttpResponseRedirect('/')

def add(request):
    if request.method=="POST":
        fm=PatientRegistraion(request.POST)
        if fm.is_valid():
            nm=fm.cleaned_data["name"]
            ph=fm.cleaned_data["phonenumber"]
            gen=fm.cleaned_data["gender"]
            fee=fm.cleaned_data["fee"]
            con=fm.cleaned_data["condition"]
            reg=User1(name=nm,phonenumber=ph,gender=gen,fee=fee,condition=con)
            reg.save()
            fm=PatientRegistraion()
    else:
        fm=PatientRegistraion()
    pat=User1.objects.all()
    return render (request,"add.html",{'fm':fm,"stu":pat})

def delete(request,id):
    if request.method=="POST":
        pi=User1.objects.get(pk=id)
        pi.delete()
        return HttpResponseRedirect('/add/')
    
def update(request,id):
    if request.method == 'POST':
        pi = User1.objects.get(pk=id)
        fm = PatientRegistraion(request.POST, instance=pi)
        if fm.is_valid():
            fm.save()
        return HttpResponseRedirect('/add/')
    else:
            pi = User1.objects.get(pk=id)
            fm = PatientRegistraion(instance=pi)
    return render(request, 'update.html', {'fm':fm})

