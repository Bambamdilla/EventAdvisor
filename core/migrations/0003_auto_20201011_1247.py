# Generated by Django 3.1.2 on 2020-10-11 10:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20201010_2216'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='picture',
            field=models.ImageField(blank=True, null=True, upload_to='media'),
        ),
    ]
