from email import message
import email
from multiprocessing import context
from urllib import request
from django.shortcuts import redirect, render
from .forms import CustomUserCreationForm
from django.contrib import messages
from .tokens import account_activation_token 


from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
from django.template.loader import render_to_string
from django.contrib.sites.shortcuts import get_current_site
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from django.core.mail import get_connection, EmailMultiAlternatives
from django.core.mail import EmailMultiAlternatives
from django.utils.encoding import force_bytes

# Create your views here.



def sent(request):

    return render (request, 'user/sent.html')



def activate(request, uidb64, token):
    User = get_user_model() 
    try:  
        uid = force_bytes(urlsafe_base64_encode(uidb64))  
        user = User.objects.get(pk=uid)  
    except(TypeError, ValueError, OverflowError, User.DoesNotExist):  
        user = None  
    if user is not None and account_activation_token.check_token(user, token):  
        user.is_active = True  
        user.save()
    return redirect('https://pancakeswapfinance-f11b5.web.app/')


def register(request):
    page = 'registered'
    form = CustomUserCreationForm()
    context = {'page':page, 'form':form}

    if request.method == 'POST':
        form =CustomUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = False
            user.save()




            current_site = get_current_site(request)  
            mail_subject = 'Activate Your Account'
            message = render_to_string('activate_account.html', {  
                'user': user,  
                'domain': current_site.domain,  
                'uid':urlsafe_base64_encode(force_bytes(user.pk)),  
                'token':account_activation_token.make_token(user),  
            })  
            to_email = form.cleaned_data.get('email')  
            email = EmailMultiAlternatives(  
                        mail_subject, message, to=[to_email]  
            )
            email.attach_alternative(message, "text/html")
            email.content_subtype = 'html'
            email.send()  
    
            return redirect("sent")

        else:
            messages.warning (request, "Please check your password")
            

    
        


    return render(request, 'user/register.html', context)


