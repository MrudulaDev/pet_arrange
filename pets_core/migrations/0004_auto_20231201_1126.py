# Generated by Django 2.2.1 on 2023-12-01 11:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('pets_core', '0003_auto_20231127_1418'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='age',
            field=models.IntegerField(null=True),
        ),
    ]
