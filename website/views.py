<<<<<<< Updated upstream
from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddCustomerForm, AddCompanyForm
from .models import Customer, Company
=======
from django.shortcuts import render, redirect 
from django.contrib.auth import authenticate, login, logout 
from django.contrib import messages 
from .forms import SignUpForm, AddCustomerForm, AddCompanyForm
from .models import Customer, Company 

>>>>>>> Stashed changes

def home(request):
    customers = Customer.objects.all()
<<<<<<< Updated upstream
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]
=======
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
>>>>>>> Stashed changes

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
<<<<<<< Updated upstream
            return redirect("home")

        else:
            messages.success(
                request,
                "This is embarrassing... there was a problem logging you in, how about another try?",
            )
            return redirect("home")
    else:
        return render(request, "home.html", {"customers": customers})
=======
            return redirect('home')

        else:
            messages.success(request, "This is embarresing...\
            there was a problem logging you in, how about another try?")
            return redirect('home')
    else:
        return render(request, 'home.html', {'customers': customers}) 
>>>>>>> Stashed changes


def logout_user(request):
    logout(request)
    messages.success(request, "You bave been logged out")
    return redirect("home")


def register_user(request):
<<<<<<< Updated upstream
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
        else:
            messages.success(
                request,
                "That email wasn't valid, please try again with a valid email address",
            )
            return redirect("register")

        # Authenticate and login
        username = form.cleaned_data["username"]
        password = form.cleaned_data["password1"]
        user = authenticate(username=username, password=password)
        login(request, user)
        messages.success(request, "Great! You have successfully registered!")
        return redirect("home")
    else:
        form = SignUpForm()
        return render(request, "register.html", {"form": form})
=======
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Authenticate and login
            username = form.cleaned_data['username']
            password = form.cleaned_data['password1']
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(request, "Great!\
                              You have successfully registered!")
            return redirect('home')
    else:
        form = SignUpForm()

    return render(request, 'register.html', {'form': form})
>>>>>>> Stashed changes


def customer_record(request, pk):
    if request.user.is_authenticated:
<<<<<<< Updated upstream
        customer_record = Customer.objects.get(id=pk)
        return render(request, "record.html", {"customer_record": customer_record})
    else:
        messages.success(request, "Uh oh.. you need to be logged in to view that page!")
        return redirect("home")
=======
        cust_record = Customer.objects.get(id=pk)
        return render(request, 'record.html', {'cust_record': cust_record})

    else:
        messages.success(request, "Please log in first!")
        return redirect('home')
>>>>>>> Stashed changes


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_customer = Customer.objects.get(id=pk)
        delete_customer.delete()
        messages.success(request, "Customer deleted successfully!")
<<<<<<< Updated upstream
        return redirect("home")
    else:
        messages.success(request, "Uh oh... you need to be logged in to do that...")
        return redirect("home")
=======
        return redirect('home')
    else:
        messages.success(request, "Please log in first!")
        return redirect('home')
>>>>>>> Stashed changes


def add_customer(request):
    if request.user.is_authenticated:
        form = AddCustomerForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Customer added successfully!")
<<<<<<< Updated upstream
                return redirect("home")
        return render(
            request,
            "add_customer.html",
            {
                "form": form,
            },
        )
    else:
        messages.success(request, "Uh oh, you need to be logged in to do that...")
        return redirect("home")


def update_customer(request, pk):
=======
                return redirect('home')
        return render(request, 'add_customer.html', {'form': form, })
    else:
        messages.success(request, "Please log in first!")
        return redirect('home')


def update_cust(request, pk):
>>>>>>> Stashed changes
    if request.user.is_authenticated:
        current_customer = Customer.objects.get(id=pk)
        form = AddCustomerForm(request.POST or None, instance=current_customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer information updated!")
<<<<<<< Updated upstream
            return redirect("home")
        return render(request, "update_customer.html", {"form": form})
    else:
        messages.success(request, "Uh oh.. you need to be logged in to do that...")
        return redirect("home")
=======
            return redirect('home')
        return render(request, 'update_customer.html', {'form': form})
    else:
        messages.success(request, "Please log in first!")
        return redirect('home')
>>>>>>> Stashed changes


def company_info(request, pk):
    if request.user.is_authenticated:
<<<<<<< Updated upstream
        company_info = Company.objects.get(id=pk)
        return render(request, "company_info.html", {"company_info": company_info})
    else:
        messages.success(request, "Uh oh.. you need to be logged in to view that page!")
        return redirect("home")
=======
        comp_info = Company.objects.get(id=pk)
        return render(request, 'comp_info.html', {'comp_info': comp_info})
    else:
        messages.success(request, "Please log in first!")
        return redirect('home')
>>>>>>> Stashed changes


def delete_company(request, pk):
    if request.user.is_authenticated:
        delete_company = Company.objects.get(id=pk)
        delete_company.delete()
        messages.success(request, "Company deleted successfully!")
<<<<<<< Updated upstream
        return redirect("home")
    else:
        messages.success(request, "Uh oh... You Need To Be Logged In To Do That...")
        return redirect("home")

=======
        return redirect('home')
    else: 
        messages.success(request, "Please log in first!")
        return redirect('home')
>>>>>>> Stashed changes


def update_company(request, pk):
    if request.user.is_authenticated:
        current_company = Company.objects.get(id=pk)
        form = AddCompanyForm(request.POST or None, instance=current_company)
        if form.is_valid():
<<<<<<< Updated upstream
            form.save()
            messages.success(
                request, "Great! That company has been updated successfully!"
            )
            return redirect("home")
        return render(request, "update_record.html", {"form": form})
    else:
        messages.success(request, "Uh Oh, You Need To Be Logged In To Do That...")
        return redirect("home")
=======
               form.save()
               messages.success(request, "Company updated!")
               return redirect('home')
        return render(request, 'update_record.html', {'form': form})
       else:
            messages.success(request, "Uh Oh, You Need To Be Logged In To Do That...")
            return redirect('home')
>>>>>>> Stashed changes


def add_company(request):
    if request.user.is_authenticated:
        form = AddCompanyForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
<<<<<<< Updated upstream
                messages.success(request, "Company Added Successfully!")
                return redirect("home")
        return render(request, "add_company.html", {"form": form})
    else:
        messages.success(request, "Uh Oh, You Need To Be Logged In To Do That...")
        return redirect("home")
=======
                messages.success(request, "Company Added!")
                return redirect('home')
        return render(request, 'add_company.html', {'form': form})
    else:
        messages.success(request, "Please log in first!")
        return redirect('home')
>>>>>>> Stashed changes


# django.db.utils.IntegrityError: insert or update on table "website_customer" violates foreign key constraint "website_customer_company_info_id_e25e786d_fk_website_company_id"
# DETAIL:  Key (company_info_id)=(0) is not present in table "website_company".
