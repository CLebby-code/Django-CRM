from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .forms import SignUpForm, AddCustomerForm, AddCompanyForm
from .models import Customer, Company


def home(request):
    customers = Customer.objects.all()
    if request.method == "POST":
        username = request.POST["username"]
        password = request.POST["password"]

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, "Login successful!")
            return redirect("home")

        else:
            messages.success(
                request,
                "This is embarrassing... there was a problem logging you in, how about another try?",
            )
            return redirect("home")
    else:
        return render(request, "home.html", {"customers": customers})


def logout_user(request):
    logout(request)
    messages.success(request, "You bave been logged out")
    return redirect("home")


def register_user(request):
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


def customer_record(request, pk):
    if request.user.is_authenticated:
        customer_record = Customer.objects.get(id=pk)
        return render(request, "record.html", {"customer_record": customer_record})
    else:
        messages.success(request, "Uh oh.. you need to be logged in to view that page!")
        return redirect("home")


def delete_record(request, pk):
    if request.user.is_authenticated:
        delete_customer = Customer.objects.get(id=pk)
        delete_customer.delete()
        messages.success(request, "Customer deleted successfully!")
        return redirect("home")
    else:
        messages.success(request, "Uh oh... you need to be logged in to do that...")
        return redirect("home")


def add_customer(request):
    if request.user.is_authenticated:
        form = AddCustomerForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Customer added successfully!")
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
    if request.user.is_authenticated:
        current_customer = Customer.objects.get(id=pk)
        form = AddCustomerForm(request.POST or None, instance=current_customer)
        if form.is_valid():
            form.save()
            messages.success(request, "Customer information updated!")
            return redirect("home")
        return render(request, "update_customer.html", {"form": form})
    else:
        messages.success(request, "Uh oh.. you need to be logged in to do that...")
        return redirect("home")


def company_info(request, pk):
    if request.user.is_authenticated:
        company_info = Company.objects.get(id=pk)
        return render(request, "company_info.html", {"company_info": company_info})
    else:
        messages.success(request, "Uh oh.. you need to be logged in to view that page!")
        return redirect("home")


def delete_company(request, pk):
    if request.user.is_authenticated:
        delete_company = Company.objects.get(id=pk)
        delete_company.delete()
        messages.success(request, "Company deleted successfully!")
        return redirect("home")
    else:
        messages.success(request, "Uh oh... You Need To Be Logged In To Do That...")
        return redirect("home")


def update_company(request, pk):
    if request.user.is_authenticated:
        current_company = Company.objects.get(id=pk)
        form = AddCompanyForm(request.POST or None, instance=current_company)
        if form.is_valid():
            form.save()
            messages.success(
                request, "Great! That company has been updated successfully!"
            )
            return redirect("home")
        return render(request, "update_record.html", {"form": form})
    else:
        messages.success(request, "Uh Oh, You Need To Be Logged In To Do That...")
        return redirect("home")


def add_company(request):
    if request.user.is_authenticated:
        form = AddCompanyForm(request.POST or None)
    if request.user.is_authenticated:
        if request.method == "POST":
            if form.is_valid():
                form.save()
                messages.success(request, "Company Added Successfully!")
                return redirect("home")
        return render(request, "add_company.html", {"form": form})
    else:
        messages.success(request, "Uh Oh, You Need To Be Logged In To Do That...")
        return redirect("home")


# django.db.utils.IntegrityError: insert or update on table "website_customer" violates foreign key constraint "website_customer_company_info_id_e25e786d_fk_website_company_id"
# DETAIL:  Key (company_info_id)=(0) is not present in table "website_company".
