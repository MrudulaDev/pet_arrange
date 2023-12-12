# Generated by Django 2.2.2 on 2023-12-11 18:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('pets_core', '0006_auto_20231208_1124'),
    ]

    operations = [
        migrations.CreateModel(
            name='Request',
            fields=[
                ('request_id', models.IntegerField(primary_key=True, serialize=False)),
                ('request_status', models.CharField(choices=[('OPEN', 'OPEN'), ('APPROVED', 'APPROVED'), ('CLOSED', 'CLOSED')], default='OPEN', max_length=20)),
                ('requested_at', models.DateTimeField(auto_now_add=True)),
                ('status_change_timestamp', models.DateTimeField(blank=True, null=True)),
                ('requested_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='pets_core.Adopter')),
                ('requested_pet', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='requests', to='pets_core.Pet')),
            ],
        ),
    ]