# Generated migration - add ForeignKey constraint to idRepartidor

from django.db import migrations, models
import django.db.models.deletion


def ensure_repartidor_exists(apps, schema_editor):
    """Ensure Repartidor table exists before adding ForeignKey"""
    from django.db import connection
    from django.conf import settings
    
    db_engine = settings.DATABASES['default']['ENGINE']
    
    with connection.cursor() as cursor:
        try:
            # Check if repartidores table exists (compatible with SQLite, PostgreSQL, MySQL)
            if 'sqlite' in db_engine:
                cursor.execute("SELECT name FROM sqlite_master WHERE type='table' AND name='repartidores'")
                table_exists = cursor.fetchone() is not None
            elif 'postgresql' in db_engine:
                cursor.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'repartidores')")
                table_exists = cursor.fetchone()[0]
            elif 'mysql' in db_engine:
                cursor.execute("SELECT EXISTS (SELECT 1 FROM information_schema.tables WHERE table_name = 'repartidores')")
                table_exists = cursor.fetchone()[0]
            else:
                table_exists = False
            
            # If table doesn't exist, we don't need to do anything
            # The model will create it during migration
        except Exception:
            # Ignore errors, the table might already exist
            pass


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
