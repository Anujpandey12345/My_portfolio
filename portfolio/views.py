from django.shortcuts import render, HttpResponse, redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, logout, login as auth_login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from portfolio import models

# Contact View
def contact(request):
   if request.method == "POST":
       print('post')
       name = request.POST.get('name')
       email = request.POST.get('email')
       content = request.POST.get('content')
       number = request.POST.get('number')
       print(name, email, number, content)

       if len(name) > 1 and len(name) < 30:
           pass
       else:
           messages.error(request, 'Length of name should be greater than 2 and less than 30 words ')
           return render(request, 'home.html')

       if len(email) > 1 and len(email) < 30:
           pass
       else:
           messages.error(request, 'Invalid email, try again ')
           return render(request, 'home.html')

       if len(number) > 9 and len(number) < 13:
           pass
       else:
           messages.error(request, 'Invalid number, please try again ')
           return render(request, 'home.html')

       # Saving the form data to the database
       ins = models.Contact(name=name, email=email, content=content, number=number)
       ins.save()
       messages.success(request, 'Thank you for contacting me! Your message has been saved.')
       print('Data has been saved to database')

   return render(request, 'home.html')

# Signup View
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

# Login View
def login_user(request):
    if request.method == 'POST':
        uname = request.POST.get('username')
        pass1 = request.POST.get('password')

        user = authenticate(request, username=uname, password=pass1)
        if user is not None:
            auth_login(request, user)
            return redirect('contact')  # Ensure 'contact' is the correct URL name
        else:
            messages.error(request, "Invalid username or password!")
            return redirect('login')
        
    return render(request, 'login.html')
