# Generated by Django 5.1.5 on 2025-01-24 06:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0002_image_name'),
    ]

    operations = [
        migrations.CreateModel(
            name='Scooter',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('image_file', models.ImageField(upload_to='scooter_images/')),
            ],
        ),
    ]
