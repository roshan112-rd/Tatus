# Generated by Django 4.0.3 on 2022-03-22 09:12

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0004_message_designatiom_alter_message_message_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='message',
            old_name='designatiom',
            new_name='designation',
        ),
    ]
