# Generated by Django 4.1.9 on 2023-07-26 07:07

from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0004_alter_customer_company_alter_note_customer'),
    ]

    operations = [
        migrations.AlterField(
            model_name='company',
            name='phone',
            field=phonenumber_field.modelfields.PhoneNumberField(blank=True, max_length=128, region=None),
        ),
    ]
