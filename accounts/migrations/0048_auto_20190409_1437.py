# Generated by Django 2.1.2 on 2019-04-09 11:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0047_auto_20190409_1436'),
    ]

    operations = [
        migrations.AlterField(
            model_name='appointment',
            name='schedule_date',
            field=models.DateField(null=True),
        ),
    ]