# Generated by Django 2.0 on 2018-02-21 08:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('clipboard', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='fileentry',
            name='file',
            field=models.FileField(upload_to=''),
        ),
    ]
