from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,logout, login as auth_login
# This decorators Use for Login If the Person is valid then enter in home Page Otherwise Not 
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from portfolio import models
from portfolio.models import Contact

# # Create your views here.



@login_required(login_url='login')
def contact(request):
   if request.method=="POST":
       print('post')
       name=request.POST.get('name')
       email=request.POST.get('email')
       content=request.POST.get('content')
       number=request.POST.get('number')
       print(name,email,number,content )

       if len(name)>1 and len(name)<30:
           pass
       else:
           messages.error(request,'Lenght of name should be greater than 2 and less than 30 words ')
           return render(request,'home.html')
       
       if len (email)>1 and len(email)<30:
           pass
       else:
           messages.error(request,'invaild email try again ')
           return render(request,'home.html')
       print(len(number))
       if  len(number)>9 and len(number)<13:
           pass
       else:
           messages.error(request,'invaild number please try again ')
           return render(request,'home.html')
       ins = models.Contact(name=name, email=email, content=content, number=number)
       ins.save()
    #    Contact.objects.create(name=name, email=email, number=number, content=content)
       messages.success(request,'Thank You for contacting me!! Your message has been saved ')
       print('data has been saved to database')
 
       print('The request is no pass ')
    
   return render(request,'home.html')


def signup(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        email = request.POST.get('email')
        pass1 = request.POST.get('password1')
        pass2 = request.POST.get('password2')
        if pass1 != pass2:
            return HttpResponse("Your Password or Confirm Password are not Same!!")
        else:
            my_user = User.objects.create_user(uname, email, pass1)
            my_user.save()
            return redirect('login')
        
    return render(request, 'signup.html')
def login_user(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pass1 = request.POST.get('password')

        user = authenticate(request, username = uname, password = pass1)
        if user is not None:
            auth_login(request, user)
            return redirect('contact')
        else:
            return HttpResponse("Password Is not Currect!!")
        
    return render(request, 'login.html')


