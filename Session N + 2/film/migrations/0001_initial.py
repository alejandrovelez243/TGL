# Generated by Django 4.2.2 on 2023-06-29 23:06

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('name', models.CharField(max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Film',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('estado', models.BooleanField(default=True)),
                ('title', models.CharField(max_length=100)),
                ('description', models.TextField()),
                ('language', models.CharField(max_length=20)),
                ('release_year', models.IntegerField()),
                ('rental_duration', models.IntegerField()),
                ('rental_date', models.DateField()),
                ('category', models.ManyToManyField(to='film.category')),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
