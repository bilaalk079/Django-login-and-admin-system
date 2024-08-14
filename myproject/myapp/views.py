from django.shortcuts import render, redirect
from django.contrib import messages
from datetime import datetime
from dateutil.parser import parse
time_millisec = datetime.now()
from myapp.models import *
from django.contrib.auth.models import User, auth
from django.contrib.auth.models import make_password
from django.contrib.auth.decorators import login_required
from rest_framework.views import APIView
from rest_framework.response import Response
from .serializers import UserInfoSerializer

# APIview
class UserInfoAPIView(APIView ):
    def get(self,request):
        store_info = UserInfo.objects.filter(is_superuser = 0 )
        serializer = UserInfoSerializer(store_info, many=True)
        return Response(serializer.data)
                        
#API (this is used call info from our website to )

# Create your views here.
def home_page(request):
    my_variable = "This is Django class right now."
    return render(request, 'index.html', {'store_var': my_variable})

def calculator(request):
    if request.method == 'POST':
        first_num = int(request.POST.get('first_num'))
        operator = request.POST.get('operator')
        second_num = int(request.POST.get('second_num'))
        answer = None

        if first_num is None or second_num is None:
            messages.info(request, "Only numbers are allowed")
            return render(request, 'calculator.html')
        else:
            if operator == "+":
                answer = first_num + second_num
            elif operator == "-":
                answer = first_num - second_num
            elif operator == "/":
                answer = first_num / second_num
            elif operator == "*":
                answer = first_num * second_num
            return render(request, 'calculator.html', {'answer': answer})
    else:
        return render(request, 'calculator.html')

def registration(request):
    if request.method == 'POST':
        get_name = request.POST.get('name')
        get_phone = request.POST.get('phone')
        get_gender = request.POST.get('gender')
        get_email = request.POST.get('email')
        get_dob = request.POST.get('dob')
        get_username = request.POST.get('username')
        get_password = request.POST.get('password')

        if User.objects.filter(username=get_username).exists() or User.objects.filter(email=get_email).exists():
            messages.info(request, 'Username or Email already exists')
        else:
            submit_user = User.objects.create_user(password=get_password, is_superuser=0, username=get_username, first_name=get_name, email=get_email)
            submit_user.save()

            user_info = UserInfo.objects.create(name=get_name, phone=get_phone, email=get_email, username=get_username, dob=get_dob, user=submit_user, gender = get_gender,is_superuser=0)
            user_info.save()
            messages.info(request, f"Thank you {get_name} for registering with us")
            return redirect('/login')
    else:
        return render(request, 'registration.html')
    
def login(request):
    if request.method == 'POST':
        get_username = request.POST.get('username')
        get_password = request.POST.get('password')

        user = auth.authenticate(username=get_username, password =get_password)
        if user is None:
            messages.info(request,"Authentication failed")
            return redirect("/login")
        else:
            auth.login(request,user)
            get_user = request.user
            get_superuser = get_user.is_superuser
            if get_superuser == 1:
                return redirect("/admin_dashboard")
            else:
                get_username = UserInfo.objects.get(username = get_user)
                get_status = get_username.status
                if get_status == "block":
                    messages.info(request,"You have been blocked from Mayapp")
                    return redirect('/logout')
                else:
                    return redirect('/dashboard')
    else:
        return render(request,"login.html")    
def logout(request):
    auth.logout(request)
    return redirect('/login')
@login_required(login_url='/login')
def dashboard(request):
    return render(request, "dashboard.html", )
@login_required(login_url='/login')
def edit_user(request):
    if request.method == 'POST':
        get_id = request.POST.get('get_id')
        get_name = request.POST.get('name')
        get_phone = request.POST.get('phone')
        get_gender = request.POST.get('gender')
        get_email = request.POST.get('email')
        get_dob1 = request.POST.get('dob')
        get_dob = parse(get_dob1)#y-m-d
        get_username = request.POST.get('username')
        get_password = request.POST.get('password')

        user_identity = User.objects.get(id= get_id)
        user_identity.first_name = get_name
        user_identity.username = get_username
        user_identity.email = get_email
        user_identity.password = make_password(get_password)
        user_identity.save()

        user_info = UserInfo.objects.get(user_id=get_id)
        user_info.phone = get_phone
        user_info.email =get_email
        user_info.username =get_username
        user_info.gender = get_gender
        user_info.dob = get_dob
        user_info.name = get_name
        user_info.save()
        messages.info(request,"your info just got updated")
        return redirect('/login')
    else:
        return render(request,'edit_user.html',)
def regadmin(request):
    if request.method == 'POST':
        get_name =request.POST.get('name')
        get_phone = request.POST.get('phone')
        get_email = request.POST.get('email')
        get_username = request.POST.get('username')
        get_password = request.POST.get('password')

        if User.objects.filter(username = get_username).exists() or User.objects.filter(email=get_email).exists():
            messages.info(request,"username or email already exists")
            return redirect('/regadmin')
        else:
            submit_admin = User.objects.create_user(password=get_password,is_superuser=1,username=get_username,email=get_email)
            submit_admin.save()

            submit_admin_info = UserInfo.objects.create(name=get_name,phone=get_phone,is_superuser =1 ,user=submit_admin)
            submit_admin_info.save()
            messages.info(request, "Admin Successfully Registered")
            return redirect('/login')
    else:
        return render(request,'regadmin.html')
@login_required(login_url='/login')
def admin_dashboard(request):
        return render(request,'admin_dashboard.html')
@login_required(login_url='/login')
def all_users(request):
    get_all_users_info = UserInfo.objects.filter(is_superuser = 0)
    return render(request, 'all_users.html',{'get_all_users_info':get_all_users_info})
@login_required(login_url='/login')
def single_user(request, id):
    single_identity = UserInfo.objects.get(id = id)
    return render(request,'single_user.html',{'single_identity':single_identity})
@login_required(login_url='/login')
def edit_admin(request):
    if request.method == 'POST':
        get_id = request.POST.get('get_id')
        get_name = request.POST.get('name')
        get_phone = request.POST.get('phone')
        get_email = request.POST.get('email')
        get_username = request.POST.get('username')
        get_password = request.POST.get('password')

        user_identity = User.objects.get(id= get_id)
        user_identity.first_name = get_name
        user_identity.username = get_username
        user_identity.email = get_email
        user_identity.password = make_password(get_password)
        user_identity.save()

        user_info = UserInfo.objects.get(user_id=get_id)
        user_info.phone = get_phone
        user_info.email = get_email
        user_info.username = get_username
        user_info.name = get_name
        user_info.save()
        messages.info(request,f"Admin {get_name} your info just got updated")
        return redirect('/login')
    else:
        return render(request,'edit_admin.html',)
def block(request, id):
    get_id  = UserInfo.objects.get(id=id)
    get_id.status = 'block'
    get_id.save()
    return redirect('/all_users')
def unblock(request,id):
    get_id  = UserInfo.objects.get(id=id)
    get_id.status = None
    get_id.save()
    return redirect('/all_users')
def delete(request,id):
    get_id  = User.objects.get(id=id)
    get_id.delete()
    return redirect('/all_users')
