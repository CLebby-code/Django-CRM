from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages 

def home (request):
    return render(request, 'home.html', {})

#def login_user request:
    #return(render, request, "authentication/login.html") 

#check if user is logging in 
def login_user(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        #Authenticate 
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login Successful!")
            return redirect('home')
        else:
            messages.success(request, "Whoops, There Was A Problem Logging You In, Please Try Again..")
            return redirect('login')
    else: 
        return render(request, 'login.html', {}) 
    

def logout_user (request):
    logout(request)
    messages.success(request, "You Have Been Logged Out")
    return redirect('home')

def register_user(request):
    return render(request, 'register.html', {})


#Request is sent to backend here, we pass it nito the view and return the homepage in the first example. 