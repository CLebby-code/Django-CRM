from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import SignUpForm, AddCustomerForm, AddCompanyForm, AddCustNote
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
                "This is embarressing... there was a problem logging you in, how about another try?",  # noqa: E501
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

            # Authenticate and login
            username = form.cleaned_data["username"]
            password = form.cleaned_data["password1"]
            user = authenticate(username=username, password=password)
            login(request, user)
            messages.success(
                request,
                "Great!\
                             You have successfully registered!",
            )
            return redirect("home")
        else:
            form = SignUpForm()

        return render(request, "register_user.html", {"form": form})


@login_required
def customer_record(request, pk):
    customer_record = Customer.objects.get(id=pk)
    return render(request, "customer_record.html", {"customer_record": customer_record})


@login_required
def delete_customer(request, pk):
    delete_customer = Customer.objects.get(id=pk)
    delete_customer.delete()
    messages.success(request, "Customer deleted successfully!")
    return redirect("home")


@login_required
def add_customer(request):
    form = AddCustomerForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Customer added successfully!")
            return redirect("home")
    else:
        return render(
            request,
            "add_customer.html",
            {
                "form": form,
            },
        )


@login_required
def update_customer(request, pk):
    current_customer = Customer.objects.get(id=pk)
    form = AddCustomerForm(request.POST or None, instance=current_customer)
    if form.is_valid():
        form.save()
        messages.success(request, "Customer information updated!")
        return redirect("home")
    else:
        return render(request, "update_customer.html", {"form": form})


@login_required
def company_list(request):
    companys = Company.objects.all()
    context = {"companys": companys}
    return render(request, "company_list.html", context)


@login_required
def company_details(request, pk):
    company_details = Company.objects.get(id=pk)
    company_customers = company_details.customers.all()
    context = {
        "company_details": company_details,
        "company_customers": company_customers,
    }
    return render(request, "company_details.html", context)


@login_required
def delete_company(request, pk):
    delete_company = Company.objects.get(id=pk)
    delete_company.delete()
    messages.success(request, "Company deleted successfully!")
    return redirect("home")


@login_required
def update_company(request, pk):
    current_company = Company.objects.get(id=pk)
    form = AddCompanyForm(request.POST or None, instance=current_company)
    if form.is_valid():
        form.save()
        messages.success(request, "Company updated!")
        return redirect("home")
    else:
        return render(request, "update_company.html", {"form": form})


@login_required
def add_company(request):
    form = AddCompanyForm(request.POST or None)
    if request.method == "POST":
        if form.is_valid():
            form.save()
            messages.success(request, "Company Added!")
            return redirect("home")

    return render(request, "add_company.html", {"form": form})


@login_required
def add_note(request):
    if request.method == "GET":
        customer_id = request.GET.get("customer", "")
        customer = Customer.objects.get(id=customer_id)
        form = AddCustNote(
            request.POST or None, initial={"customer": customer}
        )  # noqa: E501
        return render(request, "add_note.html", {"form": form})

    if request.method == "POST":
        form = AddCustNote(request.POST or None)
        if form.is_valid():
            note = form.save(commit=False)
            note.author = request.user
            note.save()
            messages.success(request, "Note saved!")
            return redirect("/customer_record/%s" % form.cleaned_data["customer"].id)
        else:
            return render(request, "add_note.html", {"form": form})
