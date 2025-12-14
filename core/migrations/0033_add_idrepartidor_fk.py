# Generated migration - add ForeignKey constraint to idRepartidor

from django.db import migrations, models
import django.db.models.deletion


def ensure_repartidor_exists(apps, schema_editor):
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
            # Create the table if it doesn't exist
            cursor.execute("""
                CREATE TABLE repartidores (
                    "idRepartidor" SERIAL PRIMARY KEY,
                    "nomberepartidor" VARCHAR(100),
                    "telefonoRepartidor" VARCHAR(20),
                    "email" VARCHAR(100)
                )
            """)


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_final_cleanup'),
    ]

    operations = [
        migrations.RunPython(ensure_repartidor_exists, migrations.RunPython.noop),
        # Alter the idRepartidor field to add ForeignKey constraint
        migrations.AlterField(
            model_name='pedido',
            name='idRepartidor',
            field=models.ForeignKey(blank=True, db_column='idrepartidor', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.repartidor'),
        ),
    ]
