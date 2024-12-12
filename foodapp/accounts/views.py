from datetime import datetime
# from django.contrib.auth.tokens import default_token_generator
# from django.core.mail import message
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
# from django.utils.http import urlsafe_base64_decode
from .forms import UserForm
from .models import User


import datetime

def home(request):
    return render(request,'home.html')

def registerUser(request):
    if request.method == 'POST':
        print(request.POST)
        form=UserForm(request.POST)
        if form.is_valid():
            print('valid')

            # user=form.save(commit=False)
            # user.set_password(password)
            # user.role=User.CUSTOMER
            # print(user)
            # form.save()
            first_name=form.cleaned_data['first_name']
            last_name=form.cleaned_data['last_name']
            username=form.cleaned_data['username']
            email=form.cleaned_data['email']
            password=form.cleaned_data['password']
            user=User.objects.create(first_name=first_name,last_name=last_name,username=username,email=email,password=password)
            user.set_password(password)
            user.role=User.VENDOR
            user.save()
            print('created sucessfully')
            return redirect('registerUser')
        else:
            print('invaild')
            form=UserForm()
            
    else:
        form =UserForm()
    context={'form':form}

    return render(request,'accounts/registerUser.html',context)