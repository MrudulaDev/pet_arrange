# Generated by Django 2.2.2 on 2023-11-20 18:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pets_core', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='pet',
            name='adopter',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, related_name='pets', to='pets_core.Adopter'),
        ),
    ]
