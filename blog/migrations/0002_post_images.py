# Generated by Django 3.2.16 on 2023-05-02 14:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='images',
            field=models.ImageField(blank=True, upload_to='mediaupload/media/', verbose_name='Upload images'),
        ),
    ]
