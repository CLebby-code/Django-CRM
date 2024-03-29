from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from django.contrib.auth.models import User

# Table with Company information


class Company(models.Model):
    name = models.CharField(max_length=50, default="name")
    website = models.CharField(max_length=50, default="website")
    phone = PhoneNumberField(blank=True)
    email = models.CharField(max_length=30, default="email")
    industry = models.CharField(max_length=100, default="industry")

    def __str__(self):
        return self.name


# Table with Customer info and FK (ID)
class Customer(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=75)
    phone = models.CharField(max_length=20)
    address = models.CharField(max_length=100)
    city = models.CharField(max_length=50)
    postcode = models.CharField(max_length=10)
    company = models.ForeignKey(
        Company, on_delete=models.CASCADE, null=True, related_name="customers"
    )
    lead_status_choices = [
        ("New", "New"),
        ("Open", "Open"),
        ("In Progress", "In progress"),
        ("Open deal", "Open deal"),
        ("Unqualified", "Unqualified"),
        ("Attempted to contact", "Attempted to contact"),
        ("Connected", "Connected"),
        ("Bad Timing", "Bad timing"),
        ("Unassigned", "Unassigned"),
    ]
    lead_status = models.CharField(
        max_length=50, choices=lead_status_choices, default="Unassigned"
    )

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Note(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    add_note = models.CharField(max_length=100)
    customer = models.ForeignKey(
        Customer, on_delete=models.CASCADE, null=True, related_name="note"
    )
    author = models.ForeignKey(
        User, on_delete=models.CASCADE, null=True, related_name="note"
    )


def __str__(self):
    return f"{self.note}"
