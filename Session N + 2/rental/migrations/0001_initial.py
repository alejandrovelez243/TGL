# Generated by Django 4.2.2 on 2023-06-29 23:06

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('film', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inventory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('film_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='film.film')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Rental',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('return_date', models.DateField()),
                ('customer_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('inventor_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='rental.inventory')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]