# Generated by Django 4.2.4 on 2023-10-12 05:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ridebooking',
            name='email',
            field=models.EmailField(default='Your Email here', max_length=255),
        ),
        migrations.AddField(
            model_name='ridebooking',
            name='phone_number',
            field=models.CharField(default='Your phone number', max_length=15),
        ),
    ]
