# Generated by Django 5.1.5 on 2025-01-24 07:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app1', '0003_scooter'),
    ]

    operations = [
        migrations.AddField(
            model_name='scooter',
            name='description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='scooter',
            name='name',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='scooter',
            name='uploaded_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='scooter',
            name='image_file',
            field=models.ImageField(upload_to='images/'),
        ),
        migrations.AlterField(
            model_name='scooter',
            name='title',
            field=models.CharField(max_length=300),
        ),
    ]
