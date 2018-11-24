# Generated by Django 2.1.2 on 2018-11-22 17:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0034_auto_20181119_1220'),
    ]

    operations = [
        migrations.AlterField(
            model_name='donor',
            name='blood_group',
            field=models.CharField(blank=True, choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], default='choose', max_length=40, null=True),
        ),
    ]
