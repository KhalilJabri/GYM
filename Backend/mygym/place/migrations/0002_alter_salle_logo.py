# Generated by Django 4.1.1 on 2022-10-01 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('place', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='salle',
            name='logo',
            field=models.FileField(blank=True, upload_to='document'),
        ),
    ]