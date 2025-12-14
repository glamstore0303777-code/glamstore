# Mark previous migration as fake since column already exists

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0055_add_fecha_vencimiento_pedido'),
    ]

    operations = [
        # This is a no-op migration to mark the previous one as applied
        # The fecha_vencimiento column already exists in the database
    ]
