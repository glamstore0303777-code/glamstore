# Generated migration - update Pedido model with new fields

from django.db import migrations, models
import django.db.models.deletion


def ensure_repartidor_table(apps, schema_editor):
    """Ensure Repartidor table exists before adding ForeignKey"""
    from django.db import connection
    with connection.cursor() as cursor:
        # Check if repartidores table exists
        cursor.execute("""
            SELECT EXISTS (
                SELECT 1 FROM information_schema.tables 
                WHERE table_name = 'repartidores'
            )
        """)
        if not cursor.fetchone()[0]:
            # If table doesn't exist, create it
            cursor.execute("""
                CREATE TABLE repartidores (
                    idRepartidor SERIAL PRIMARY KEY,
                    nomberepartidor VARCHAR(100),
                    telefonoRepartidor VARCHAR(20),
                    email VARCHAR(100)
                )
            """)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_detallepedido_margen_ganancia'),
    ]

    operations = [
        migrations.RunPython(ensure_repartidor_table, migrations.RunPython.noop),
        # Add idRepartidor field to Pedido
        migrations.AddField(
            model_name='pedido',
            name='idRepartidor',
            field=models.ForeignKey(blank=True, db_column='idrepartidor', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.repartidor'),
        ),
    ]
