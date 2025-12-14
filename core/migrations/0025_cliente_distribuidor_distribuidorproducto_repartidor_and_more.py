# Generated migration - create additional models

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_producto_precio_venta'),
    ]

    operations = [
        # Repartidor, Distribuidor, and DistribuidorProducto already created in 0004
        # This migration is a no-op placeholder
        migrations.RunPython(lambda apps, schema_editor: None, migrations.RunPython.noop),
    ]
