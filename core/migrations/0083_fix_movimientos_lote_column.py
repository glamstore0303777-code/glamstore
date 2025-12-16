from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0082_ensure_mensajes_contacto_table'),
    ]

    operations = [
        migrations.RunSQL(
            sql="ALTER TABLE movimientos_lote ADD COLUMN IF NOT EXISTS movimiento_producto_id INTEGER;",
            reverse_sql=migrations.RunSQL.noop,
        ),
    ]
