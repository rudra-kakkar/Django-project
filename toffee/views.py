from django.shortcuts import render
from django.http import HttpResponse
from .models import Toffee
from .forms import ToffeeForm, UserRegistrationForm
from django.shortcuts import get_object_or_404,redirect,render
from django.contrib.auth.decorators import login_required
from django.contrib.auth import login
from django.core.mail import send_mail
from django.conf import settings
from .forms import ContactForm

def index(request):
    return render(request,'index.html')

def about(request):
    return render(request,'about.html')

# def contact(request):
#     return render(request, 'contact.html')

def toffee_list(request):
    toffees = Toffee.objects.all().order_by("-created_at")
    return render(request,'toffee_list.html',{'toffees':toffees})

@login_required
def toffee_create(request):
    if request.method == "POST":
        form = ToffeeForm(request.POST, request.FILES)
        if form.is_valid():
            toffee = form.save(commit=False)
            toffee.user = request.user
            toffee.save()
            return redirect('toffee_list')
    else:
        form = ToffeeForm()
    return render(request,"toffee_form.html",{"form":form})

@login_required
def toffee_edit(request,toffee_id):
    toffee = get_object_or_404(Toffee,pk = toffee_id, user = request.user)
    if request.method == "POST":
        form = ToffeeForm(request.POST, request.FILES, instance=toffee )
        if form.is_valid():
            toffee = form.save(commit=False)
            toffee.user = request.user
            toffee.save()
            return redirect('toffee_list')
    else:
        form = ToffeeForm(instance=toffee)
    return render(request,"toffee_form.html",{"form":form})

@login_required
def toffee_del(request,toffee_id):
    toffee = get_object_or_404(Toffee,pk = toffee_id, user = request.user)
    if request.method == 'POST':
        toffee.delete()
        return redirect('toffee_list')
    return render(request,"toffee_del.html",{"toffee": toffee})

def register(request):
    if request.method == "POST":
        form = UserRegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(form.cleaned_data['password1'])
            user.save()
            login(request, user)
            return redirect('toffee_list')
    else:
        form = UserRegistrationForm()

        
    return render(request, 'registration/register.html',{'form':form})


def contact(request):
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            message = form.cleaned_data['message']

            # Sending the email
            send_mail(
                subject=f'Contact Form Query from {name}',
                message=message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=[settings.EMAIL_HOST_USER],  # Your email
                fail_silently=False,
            )

            return render(request, 'thanks.html')  # Redirect to a 'Thank You' page
    else:
        form = ContactForm()

    return render(request, 'contact.html', {'form': form})

