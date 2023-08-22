from django.shortcuts import render,redirect
from django.contrib import messages
from .models import Inscription
from django.core.mail import send_mail,EmailMultiAlternatives
from django.conf import settings


# Create your views here.

def accueil(request):
    inscription = Inscription.objects.all()

    return render(request,'ecole/accueil.html',{'inscription':inscription})
    



def page(request):  
    return render(request,'ecole/page.html')

def saveinscription(request):
    return render(request,'ecole/iscription.html')

def inscription(request):
    if request.method == 'POST':
        non = request.POST.get("nom")
        email = request.POST.get("email")
        numero = request.POST.get("number")
        dates = Inscription.objects.create(nom=non, email=email,numero=numero)
        dates.save()
        messages.success(request,'felicitation inscription creer avec success')
        
        
    return render(request,'ecole/accueil.html',{'messages':messages})


def deleteuser(request, pk):
    obj = Inscription.objects.get(pk=pk)
    obj.delete()
    return redirect('accueil')

def updateuser(request, pk):
    obj = Inscription.objects.get(pk=pk)
    if request.method == 'POST':
        nom = request.POST.get("nom")
        obj.nom=nom
        obj.save()
        return redirect('accueil')
    return render(request,'ecole/page.html')
    
    
    
    return render(request,'ecole/page.html',{'obj':obj})


def page(request):
    subject = 'emploie'
    msgs = request.POST.get('message')
    text_content = f"hello {request.user} {msgs} "
    recepteur = request.POST.get('email')
    recipient_list = [recepteur]
    # html_content = f"<h1>bienvenue</h1>"
    from_email = settings.EMAIL_HOST_USER
    msg = EmailMultiAlternatives(subject, text_content, from_email, recipient_list)
    
    msg.send()
    
    return render(request,'ecole/page.html')

def send_mail_user(request):
    return render(request, 'ecole/page.html')
    