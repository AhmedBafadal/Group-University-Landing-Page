from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
# Create your views here.
def about(request):
    return render(request, 'about.html', {})