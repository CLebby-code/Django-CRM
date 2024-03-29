# Generated by Django 4.1.9 on 2023-08-08 22:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    dependencies = [
        ("website", "0011_alter_contact_customer"),
    ]

    operations = [
        migrations.AddField(
            model_name="customer",
            name="lead_status",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="customers",
                to="website.contact",
            ),
        ),
        migrations.AlterField(
            model_name="contact",
            name="customer",
            field=models.ForeignKey(
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                related_name="customers",
                to="website.customer",
            ),
        ),
    ]
