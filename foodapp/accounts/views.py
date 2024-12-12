from datetime import datetime
# from django.contrib.auth.tokens import default_token_generator
# from django.core.mail import message
from django.http.response import HttpResponse
from django.shortcuts import redirect, render
# from django.utils.http import urlsafe_base64_decode


import datetime

def home(request):
    return render(request,'home.html')
