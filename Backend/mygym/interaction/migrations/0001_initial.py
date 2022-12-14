# Generated by Django 4.1.1 on 2022-09-14 02:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Activite',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('libelleAct', models.CharField(max_length=70)),
                ('etat', models.BooleanField(default=True)),
            ],
        ),
        migrations.CreateModel(
            name='Abonnement',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('dateDebutAbo', models.DateTimeField()),
                ('dateFinAbo', models.DateTimeField()),
                ('tarifAbo', models.FloatField()),
                ('act', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='activiteFK', to='interaction.activite')),
                ('membre', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='membreFK', to='account.membre')),
            ],
        ),
    ]
