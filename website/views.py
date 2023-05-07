from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages 
from .forms  import SignUpForm
from .models import Customer



def home(request):
        customers = Customer.objects.all()
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
             #Authenticate 
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                messages.success(request, "Login Successful!")
                return render(request,'home.html')
            else:
                messages.success(request, "Whoops, There Was A Problem Logging You In, Please Try Again..")
                return ('home')
        else: 
            return render(request, 'home.html', {'customers':Customer}) 
        
def logout_user (request):
    logout(request)
    messages.success(request, "You Have Been Logged Out")
    return redirect('home')

def register_user(request):
        if request.method == 'POST':
                form = SignUpForm(request.POST)
                if form.is_valid():
                        form.save()
                #Authenticate and login
                username= form.cleaned_data['username']
                password = form.cleaned_data['password1']
                user = authenticate(username=username, password=password)
                login(request, user)
                messages.success(request, "You Have Successfully Registered! Welcome!")
                return redirect('home')
        else:
                form=SignUpForm()
                return render(request, 'register.html', {'form':form})
        

#Request is sent to backend here, we pass it nito the view and return the homepage in the first example. 


