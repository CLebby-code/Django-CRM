from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from phonenumber_field.formfields import PhoneNumberField
from .models import Customer, Company, Note


class SignUpForm(UserCreationForm):
    email = forms.EmailField(
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Email Address"}
        )
    )
    first_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "First Name"}
        ),
    )
    last_name = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": "Last Name"}
        ),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "first_name",
            "last_name",
            "email",
            "password1",
            "password2",
        )

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields["username"].widget.attrs["class"] = "form-control"
        self.fields["username"].widget.attrs["placeholder"] = "User Name"
        self.fields[
            "username"
        ].help_text = '<span class="form-text text-muted"><small>Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.</small></span>'  # noqa: E501

        self.fields["password1"].widget.attrs["class"] = "form-control"
        self.fields["password1"].widget.attrs["placeholder"] = "Password"
        self.fields["password1"]
        self.fields[
            "password1"
        ].help_text = "<ul class=\"form-text text-muted small\"><li>Your password can't be too similar to your other personal information.</li><li>Your password must contain at least 8 characters.</li><li>Your password can't be a commonly used password.</li><li>Your password can't be entirely numeric.</li></ul>"  # noqa: E501

        self.fields["password2"].widget.attrs["class"] = "form-control"
        self.fields["password2"].widget.attrs[
            "placeholder"
        ] = "Confirm Password"  # noqa: E501
        self.fields["password2"]


class AddCustomerForm(forms.ModelForm):
    first_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "First Name", "class": "form-control"}
        ),
        min_length=3,
        max_length=20,
        label="",
    )
    last_name = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Last Name", "class": "form-control"}
        ),
        min_length=3,
        max_length=20,
        label="",
    )
    email = forms.EmailField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Email", "class": "form-control"}
        ),
        label="",
    )
    phone = forms.IntegerField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Phone", "class": "form-control"}
        ),
        label="",
    )
    address = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Address", "class": "form-control"}
        ),
        min_length=10,
        max_length=40,
        label="",
    )
    city = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "City", "class": "form-control"}
        ),
        min_length=5,
        max_length=10,
        label="",
    )
    postcode = forms.CharField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Postcode", "class": "form-control"}
        ),
        min_length=6,
        max_length=8,
        label="",
    )

    class Meta:
        model = Customer
        exclude = ("user",)


class AddCompanyForm(forms.ModelForm):
    name = forms.CharField(
        min_length=3,
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Name", "class": "form-control"}
        ),
        label="",
    )
    website = forms.CharField(
        min_length=9,
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Website", "class": "form-control"}
        ),
        label="",
    )

    email = forms.EmailField(
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Email", "class": "form-control"}
        ),
        label="",
    )
    industry = forms.CharField(
        min_length=5,
        required=True,
        widget=forms.widgets.TextInput(
            attrs={"placeholder": "Industry", "class": "form-control"}
        ),
        label="",
    )
    phone = PhoneNumberField(region="GB")
    phone.error_messages["invalid"] = "Please enter a valid mobile or landline number"

    class Meta:
        model = Company
        exclude = ("organisation",)


class AddCustNote(forms.ModelForm):
    add_note = forms.CharField(
        max_length=100,
        widget=forms.TextInput(
            attrs={"class": "form-control", "placeholder": ""}
        ),  # noqa: E501
    )

    customer = forms.ModelChoiceField(
        queryset=Customer.objects.all(), widget=forms.HiddenInput
    )

    class Meta:
        model = Note
        fields = "__all__"
