# Generated migration to add missing columns to movimientos_producto table

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0017_remove_pedido_fecha_detallepedido_idpedido_and_more'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            ALTER TABLE movimientos_producto
            ADD COLUMN IF NOT EXISTS lote VARCHAR(100) NULL,
            ADD COLUMN IF NOT EXISTS fecha_vencimiento DATE NULL,
            ADD COLUMN IF NOT EXISTS total_con_iva DECIMAL(10, 2) NULL,
            ADD COLUMN IF NOT EXISTS iva DECIMAL(10, 2) NULL;
            """,
            reverse_sql="""
            ALTER TABLE movimientos_producto
            DROP COLUMN IF EXISTS lote,
            DROP COLUMN IF EXISTS fecha_vencimiento,
            DROP COLUMN IF EXISTS total_con_iva,
            DROP COLUMN IF EXISTS iva;
            """
        ),
    ]
