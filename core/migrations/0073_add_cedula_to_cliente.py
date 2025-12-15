# Generated migration to add cedula field to Cliente

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0072_add_total_con_iva_to_lotes'),
    ]

    operations = [
        migrations.AddField(
            model_name='cliente',
            name='cedula',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
