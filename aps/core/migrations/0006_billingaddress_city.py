# Generated by Django 2.2.10 on 2020-06-29 08:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0005_auto_20200629_1337'),
    ]

    operations = [
        migrations.AddField(
            model_name='billingaddress',
            name='city',
            field=models.CharField(max_length=255, null=True),
        ),
    ]
