# Generated by Django 3.2 on 2021-04-13 13:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schemas', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dataset',
            name='csv_file',
            field=models.FileField(blank=True, upload_to='csv/'),
        ),
    ]