# Generated by Django 4.0.3 on 2022-03-28 11:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0011_rename_twitter_team_linkedin'),
    ]

    operations = [
        migrations.CreateModel(
            name='Subscription',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('email', models.EmailField(max_length=100)),
            ],
        ),
    ]
