# Generated by Django 4.2 on 2023-04-27 02:20

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_alter_user2_email'),
    ]

    operations = [
        migrations.RenameField(
            model_name='user2',
            old_name='phonenumber',
            new_name='Phonenumber',
        ),
    ]
