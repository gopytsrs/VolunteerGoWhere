# Generated by Django 3.0.5 on 2022-03-21 18:33

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('OrgView', '0002_auto_20220321_1741'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='campaign',
            name='duration',
        ),
        migrations.AddField(
            model_name='campaign',
            name='end_time',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
