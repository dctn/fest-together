# Generated by Django 5.1 on 2024-09-06 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('event', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event_details',
            name='event_image',
            field=models.ImageField(max_length=1000, upload_to=''),
        ),
    ]
