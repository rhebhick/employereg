# Generated by Django 4.2.7 on 2024-05-27 06:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0006_product'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='img',
            field=models.FileField(null=True, upload_to=''),
        ),
    ]
