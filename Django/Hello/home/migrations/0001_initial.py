# Generated by Django 4.1.3 on 2022-11-11 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=80)),
                ('email', models.CharField(max_length=80)),
                ('phone', models.CharField(max_length=50)),
                ('desc', models.TextField()),
                ('date', models.DateField()),
            ],
        ),
    ]
