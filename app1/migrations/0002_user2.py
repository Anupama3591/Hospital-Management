# Generated by Django 4.2 on 2023-04-27 01:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='User2',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=355)),
                ('phonenumber', models.IntegerField(max_length=10)),
                ('email', models.EmailField(max_length=254)),
                ('subject', models.CharField(max_length=355)),
                ('message', models.CharField(max_length=355)),
            ],
        ),
    ]
