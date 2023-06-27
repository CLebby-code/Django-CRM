from django.contrib import admin
from .models import Customer
from .models import Company
from .models import Note

admin.site.register(Customer)
admin.site.register(Company)
admin.site.register(Note)