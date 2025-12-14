# Generated migration - fecha_vencimiento already exists in database
# This is a no-op migration to mark the state as applied

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0069_add_correo_pendiente_model'),
    ]

    operations = [
        # No-op: fecha_vencimiento column already exists in movimientos_producto table
    ]
