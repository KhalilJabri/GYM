# Generated by Django 4.1.1 on 2022-09-14 02:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('account', '0002_alter_person_cinper_alter_person_numerotelper'),
    ]

    operations = [
        migrations.AlterField(
            model_name='person',
            name='cinPer',
            field=models.FloatField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='person',
            name='numeroTelPer',
            field=models.FloatField(blank=True, null=True),
        ),
    ]
