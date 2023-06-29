# Generated by Django 4.1.7 on 2023-04-23 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('hotels', '0008_alter_hotel_rating'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='booking',
            name='check_in_date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='check_out_date',
        ),
        migrations.RemoveField(
            model_name='booking',
            name='user',
        ),
        migrations.AddField(
            model_name='booking',
            name='email',
            field=models.EmailField(default='', max_length=255),
        ),
    ]
