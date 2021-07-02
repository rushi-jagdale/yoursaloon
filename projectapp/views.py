from django.shortcuts import render,redirect
from django.contrib.auth import logout
from django.views import View
from django.core.mail import send_mail
from django.contrib.auth.models import User,auth
import uuid
from django.conf import settings
from django.contrib import messages
from .models import Profile

# Create your views here.
def index(request):
    return render(request,'base.html')

def home(request):
    return render(request,'home.html')    

def login(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username = username, password = password)
        if user is not None:
            auth.login(request, user)  
            messages.info(request, 'Success: You are now logged in.') 
            return redirect('home')

        else:
            messages.info(request, 'User does not exist!!')
            return redirect('login')
   
    else:
        return render(request,'login.html')  
      

def send_email_after(email,token):
    subject ="verify email"
    message=f'Hi click on the link to verify your account http://127.0.0.1:8000/account-verify/{token}' 
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject=subject,message=message,from_email=from_email,recipient_list=recipient_list)


class Register(View):
    def get(self,request):
        return render(request,'register.html')   

    def post(self,request):
        username = request.POST['username']
        email= request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        if password1 == password2:
            if User.objects.filter(username = username).exists():
                messages.info(request, 'username already taken..')
               
                return redirect('register')

            elif User.objects.filter(email = email).exists():
                messages.info(request, 'Email already taken ..')
                
                return redirect('register')

            else: 
                us = User.objects.create_user(username=username,email=email, password=password1)
                us.save()
                uid = uuid.uuid4()
                print(us)
                print(uid)
                pro_obj = Profile(user=us,token=uid)
                pro_obj.save()
                send_email_after(us.email,uid)
                messages.info(request, 'User Created Successfully check your email.. ')
                print('user created')
                return redirect('register')

        else:
            messages.info(request, 'Password is not matching ..')
            print('password not matching')
            return redirect('register')
    
def account_verify(request,token):
    pf=Profile.objects.filter(token=token).first()
    pf.verify = True
    pf.save()
    print(pf)
    messages.success(request, "your account has been verified , you can login")
    return redirect('/register')   

def logout(request):
    
    auth.logout(request)
    messages.success(request, " your account has been logout ")
    return redirect('home')  

      
def location(request):
    return render(request,'location.html')  

def shop(request):
    return render(request,'shop_details.html')      

def cart(request):
    return render(request,'cart.html')          