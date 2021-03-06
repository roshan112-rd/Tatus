# Generated by Django 4.0.4 on 2022-07-22 06:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('features', '0013_logo'),
    ]

    operations = [
        migrations.CreateModel(
            name='Gallery',
            fields=[
                ('event_id', models.AutoField(primary_key=True, serialize=False)),
                ('event_title', models.CharField(max_length=1000, null=True)),
                ('image1', models.ImageField(null=True, upload_to='gallery_images/')),
                ('image2', models.ImageField(null=True, upload_to='gallery_images/')),
                ('created', models.DateTimeField(auto_now_add=True, null=True)),
            ],
        ),
        migrations.DeleteModel(
            name='Event',
        ),
    ]
