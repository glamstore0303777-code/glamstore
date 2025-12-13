# Generated migration - remove margen_ganancia from Producto (moved to ConfiguracionGlobal)

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0027_configuracion_global'),
    ]

    operations = [
        # margen_ganancia was never actually added to Producto model
        # This migration is a no-op for compatibility
    ]
