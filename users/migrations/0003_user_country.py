# Generated by Django 4.1.4 on 2023-01-01 01:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("users", "0002_user_ipaddress"),
    ]

    operations = [
        migrations.AddField(
            model_name="user",
            name="country",
            field=models.CharField(blank=True, max_length=20),
        ),
    ]
