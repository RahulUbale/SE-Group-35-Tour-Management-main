# Generated by Django 4.1.7 on 2023-04-16 19:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('flights', '0003_flight_price'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='reservation',
            name='passenger',
        ),
        migrations.AddField(
            model_name='flight',
            name='no_of_seats',
            field=models.IntegerField(default=54),
        ),
        migrations.AddField(
            model_name='reservation',
            name='email',
            field=models.EmailField(default='', max_length=255, unique=True),
        ),
        migrations.AddField(
            model_name='reservation',
            name='passengers',
            field=models.IntegerField(default=1),
        ),
        migrations.AlterField(
            model_name='flight',
            name='price',
            field=models.IntegerField(default=100),
        ),
        migrations.DeleteModel(
            name='Passenger',
        ),
    ]