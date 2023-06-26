from django.db import models


# Table with Company information
class Company(models.Model):
    name = models.CharField(max_length=50, default="name")
    website = models.CharField(max_length=50, default="website")
    phone = models.CharField(max_length=20, default="phone")
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
    company = models.ForeignKey(Company, on_delete=models.CASCADE, null=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name}"


class Notes(models.Model):
    Customer_notes = models.ForeignKey(Customer, on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    add_note = models.CharField(max_length=100)


def __str__(self):
    return f"{self.notes}"
