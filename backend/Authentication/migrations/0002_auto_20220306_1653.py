# Generated by Django 3.0.5 on 2022-03-06 16:53

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('Authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ban',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Login',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=254, unique=True)),
                ('password', models.EmailField(max_length=200)),
            ],
        ),
        migrations.CreateModel(
            name='OrgAccount',
            fields=[
                ('user_id', models.BigAutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.EmailField(max_length=254)),
                ('email_confirmed', models.BooleanField(default=False)),
                ('phone_number', models.IntegerField(unique=True)),
                ('phone_number_confirmed', models.BooleanField(default=False)),
                ('address', models.CharField(max_length=200)),
                ('verified', models.BooleanField(default=False)),
            ],
        ),
        migrations.CreateModel(
            name='OTPVerfification',
            fields=[
                ('phone_number', models.IntegerField(primary_key=True, serialize=False)),
                ('otp', models.CharField(default='invalid', max_length=6)),
                ('time_of_otp', models.DateTimeField(default=django.utils.timezone.now)),
            ],
        ),
        migrations.RemoveField(
            model_name='useraccount',
            name='banned',
        ),
    ]