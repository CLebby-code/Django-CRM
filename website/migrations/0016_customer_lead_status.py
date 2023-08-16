# Generated by Django 4.1.9 on 2023-08-09 18:53

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0015_remove_customer_lead_status_delete_contact"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="lead_status",
            field=models.CharField(
                choices=[
                    ("New", "NEW"),
                    ("Open", "OPEN"),
                    ("In Progress", "IN_PROGRESS"),
                    ("Open deal", "OPEN_DEAL"),
                    ("Unqualified", "UNQUALIFIED"),
                    ("Attempted to contact", "ATTEMPTED_TO_CONTACT"),
                    ("Connected", "CONNECTED"),
                    ("Bad Timing", "BAD_TIMING"),
                    ("Unassigned", "UNASSIGNED"),
                ],
                default="NEW",
                max_length=50,
            ),
        ),
    ]
