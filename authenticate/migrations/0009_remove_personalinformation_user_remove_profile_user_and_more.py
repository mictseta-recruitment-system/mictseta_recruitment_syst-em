# Generated by Django 4.2.11 on 2024-06-06 21:43

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('authenticate', '0008_addressinformation_street_address_line1_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='personalinformation',
            name='user',
        ),
        migrations.RemoveField(
            model_name='profile',
            name='user',
        ),
        migrations.DeleteModel(
            name='AddressInformation',
        ),
        migrations.DeleteModel(
            name='PersonalInformation',
        ),
        migrations.DeleteModel(
            name='Profile',
        ),
    ]