from django.shortcuts import render,redirect
from django.http import HttpResponse
from home.models import Message
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout
import pywhatkit
import datetime
from django.core.mail import send_mail
# Create your views here.
def home(request):
    sus={'success_1':False}
    if request.method=="POST":
        is_private = request.POST.get('is_private', False)
        Code=request.POST["code"]
        mes=request.POST["Message"]
        number=request.POST["Number"]
        num1=[]
        num1=(number.split(","))
        now = datetime.datetime.now()
        for i in num1:
            pywhatkit.sendwhatmsg_instantly(str(Code)+str(i), mes,10)
            ins=Message(Number=i,Message=mes,coutntry_code=Code)
            ins.save()
        sus={'success_1':True}
        return render(request,"home.html",sus)
    return render(request,"home.html")


def Signup(request):
        if request.method=="POST":
            email=request.POST['email']
            username=request.POST['username']
            password=request.POST['pass']
            password_c=request.POST['pass1']
            
            if len(username)>15:
                Message.error(request,"userName is too long")
                
            if password!=password_c:
                Message.error(request,"password doesn't match")
                
            my_user=User.objects.create_user(username,email,password)    
            my_user.save()
        return render(request ,"signup.html")

def Login(request):
    if request.method=="POST":
        is_private = request.POST.get('is_private', False)
        password1=request.POST['passwords']
        userName_1=request.POST['userName_2']
        result=authenticate(username=userName_1,password=password1)
        if result is not None:
            name={'username2':"userName_1"}
            return render(request,"home.html",name)
        else:
             return render(request,"login.html")     

    return render(request,"login.html")

def About(request):
    return render(request,"about.html")    

def logout(request):
    logout(request)
    return redirect("login.html")    

def email_1(request):
    if request.method=="POST":
        is_private = request.POST.get('is_private', False)
        mail_subject=request.POST['subject']
        mail_email_receiver=request.POST['email']
        mail_email_sender=None
        mail_message=request.POST['message']
        email=[]
        email=(mail_email_receiver.split(","))
        send_mail(mail_subject, mail_message,mail_email_sender,email)
        return render(request,"email.html")
    return render(request,"email.html")    