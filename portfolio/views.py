from django.shortcuts import render, redirect, HttpResponse
from .models import Project
from datetime import datetime
from django.core.mail import send_mail
time = datetime.now()
year = time.year
def home(request):
    projects = Project.objects.all()
    return render(request,'portfolio/home.html', {"projects": projects, "year": year})

def contact(request):
    if request.method == 'POST':
        subject = request.POST.get('subject')
        message = request.POST.get('message')
        email = request.POST.get('email')

        if subject and message and email:
            try:
                send_mail(
                    subject,
                    message,
                    email,
                    ["edvinperfundi21@gmail.com"],
                    fail_silently=False,
                )
                return HttpResponse('Email sent successfully!')  
            except Exception as e:
                return HttpResponse(f'An error occurred: {str(e)}')
        else:
            return HttpResponse('Please fill in all required fields.')
    else:
        return render(request, 'contact_form.html')  