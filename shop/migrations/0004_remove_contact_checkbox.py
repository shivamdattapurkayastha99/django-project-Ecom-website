# Generated by Django 3.0.7 on 2020-07-01 16:44

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('shop', '0003_contact'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='checkbox',
        ),
    ]
