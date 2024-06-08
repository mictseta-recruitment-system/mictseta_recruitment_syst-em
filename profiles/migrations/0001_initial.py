# Generated by Django 4.2.11 on 2024-06-06 21:43

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idnumber', models.CharField(max_length=13, unique=True)),
                ('phone', models.CharField(max_length=10, null=True, unique=True)),
                ('gender', models.CharField(max_length=6, null=True)),
                ('age', models.CharField(max_length=6, null=True)),
                ('is_verified', models.BooleanField(default=False)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='PersonalInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('linkedin_profile', models.CharField(max_length=225)),
                ('personal_website', models.CharField(max_length=225)),
                ('job_title', models.CharField(max_length=225)),
                ('current_employer', models.CharField(max_length=225)),
                ('years_of_expreince', models.CharField(max_length=100)),
                ('industry', models.CharField(max_length=225)),
                ('carear_level', models.CharField(max_length=225)),
                ('desired_job', models.CharField(max_length=225)),
                ('job_location', models.CharField(max_length=225, null=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='AddressInformation',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street_address_line', models.CharField(max_length=225)),
                ('street_address_line1', models.CharField(max_length=225, null=True)),
                ('city', models.CharField(max_length=225)),
                ('province', models.CharField(max_length=225)),
                ('postal_code', models.CharField(max_length=6)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
