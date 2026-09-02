from django.shortcuts import render
from .models import Contact,User
from django.http import HttpResponse
from django.core.mail import send_mail
from django.conf import settings
import random

# Create your views here.
# function creates

def index(request):
    return render(request,'index.html')

def contact(request):
    if request.method == "POST":
        # ORM Query : object rational magnate
        Contact.objects.create(
            name=request.POST['name'],
            email=request.POST['email'],
            mobile=request.POST['mobile'],
            remarks=request.POST['remarks']
        )
        msg='Contact Saved Successfully'
        contacts = Contact.objects.all().order_by("-id")
        return render(request,'contact.html',{'msg':msg,'contacts':contacts})
    else:
        #get data
        contacts = Contact.objects.all().order_by("-id")
        return render(request,'contact.html',{'contacts':contacts})

def signup(request):
    if request.method=="POST":
        try:
            # email alreay hoy to aa code
            user = User.objects.get(email = request.POST['email'])
            msg = "User Already Exists"
            return render(request,'signup.html',{'msg':msg})
        except User.DoesNotExist:
            #na hot new banavase
            if request.POST['password'] == request.POST['cpassword']:
                User.objects.create(
                    fname = request.POST['fname'],
                    lname = request.POST['lname'],
                    email = request.POST['email'],
                    password = request.POST['password'],
                    mobile = request.POST['mobile'],
                    address = request.POST['address'],
                    profile_picture = request.FILES['profile_picture'],
                )
                msg = "User Registered Successfully"
                return render(request,'signup.html',{'msg':msg})
    else:
        msg = "Password amd Confrim Password does not match"
        return render(request,'signup.html',{'msg':msg})

def login(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email = request.POST['email'])
            if user.password == request.POST['password']:
                #session create thay : proccess aread succees fully login
                request.session['email']=user.email
                request.session['fname']=user.fname
                request.session['profile_picture']=user.profile_picture.url
                return render(request,'index.html')
            else:
                msg="Incorrect Password"
                return render(request,'login.html',{'msg':msg})
        except:
            msg ="Email Not Registered"
            return render(request,'login.html',{'msg':msg})
    else:
        return render(request,'login.html')

def logout(request):
    try:
        del request.session['email']
        del request.session['fname']
        del request.session['profile_picture']
        msg="User logout Successfully"
        return render(request,'login.html',{'msg':msg})
    except:
        msg="User logout Successfully"
        return render(request,'login.html',{'msg':msg})

def change_password(request):
    user = User.objects.get(email= request.session['email'])
    if request.method == "POST":
            # old password and user nakhe smae hove joei ye
            if user.password == request.POST['old_password']:
                # new and cnew match na hoy to
                if request.POST['new_password'] == request.POST['cnew_password']:
                    # 3 input same passsword nakho to change na kare
                    if user.password != request.POST['new_password']:
                        user.password = request.POST['new_password']
                        user.save()
                        del request.session['email']
                        del request.session['fname']
                        del request.session['profile_picture']
                        msg="Password Changed Successfully"
                        return render(request,'login.html',{'msg':msg})
                    else:
                        msg="Your New Password Can't be your old password"
                        return render(request,'change-password.html',{'msg':msg})
                else:
                    msg="New Password and Confirm password Does not Match"
                    return render(request,'change-password.html',{'msg':msg})
            else:
                msg="Old Password incorrect"
                return render(request,'change-password.html',{'msg':msg})
    else:
        return render(request,'change-password.html')

def forget_password(request):
    if request.method == "POST":
        try:
            user = User.objects.get(email = request.POST['email'])
            address = user.email
            subject = 'OTP for Forget Password'
            otp = str(random.randint(1000,9999))
            message = 'Your OTP for Forget pass word is '+otp
            send_mail(subject, message, settings.EMAIL_HOST_USER, [address,])
            request.session['email_to'] = user.email
            request.session['otp']=otp
            return render(request,'otp.html')

        except:
            msg="Email Not Registered"
            return render(request,'forget-password.html',{'msg':msg})
    else:
        return render(request,'forget-password.html')


def verify_otp(request):
    otp1= int(request.session['otp'])
    otp2 =int(request.POST['otp'])
    if otp1 == otp2:
        del request.session['otp']
        return render(request,'new-password.html')
    else:
        msg="Invalid OTP"
        return render(request,'otp.html',{'msg':msg})


def new_password(request):
    if request.POST['new_password'] == request.POST['cnew_password']:
        user = User.objects.get(email=request.session['email_to'])
        user.password = request.POST['new_password']
        user.save()
        del request.session['email_to']
        msg="Password Changed Successfully"
        return render(request,'login.html',{'msg':msg})
    else:
        msg="New Password & Confirm Password Does Not Matched"
        return render(request,'new-password.html',{'msg':msg})


def profile(request):
    user = User.objects.get(email=request.session['email'])
    if request.method == "POST":
        user.fname=request.POST['fname']
        user.lname=request.POST['lname']
        user.mobile=request.POST['mobile']
        user.address=request.POST['address']
        try:
            user.profile_picture= request.FILES['profile_picture']
        except:
            pass
        user.save()
        msg="Profile Updated successfully"
        request.session['fname'] = user.fname
        request.session['profile_picture']=user.profile_picture.url
        return render(request,'profile.html',{'msg':msg})

    return render(request,'profile.html',{'user':user})