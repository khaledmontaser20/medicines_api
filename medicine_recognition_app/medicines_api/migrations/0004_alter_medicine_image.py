# Generated by Django 4.2.1 on 2023-06-10 19:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('medicines_api', '0003_medicine_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='medicine',
            name='image',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]
