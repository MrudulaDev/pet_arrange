# Generated by Django 2.2.2 on 2023-11-23 09:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('pets_core', '0005_auto_20231121_1233'),
    ]

    operations = [
        migrations.RenameField(
            model_name='pet',
            old_name='category',
            new_name='pet_category',
        ),
    ]
