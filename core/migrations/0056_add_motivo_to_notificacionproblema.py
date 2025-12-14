# Generated migration

from django.db import migrations, models
from django.conf import settings


def add_motivo_field(apps, schema_editor):
    """Agregar campo motivo si no existe"""
    from django.db import connection
    
    db_engine = settings.DATABASES['default']['ENGINE']
    
    with connection.cursor() as cursor:
        try:
            if 'postgresql' in db_engine:
                cursor.execute("""
                    ALTER TABLE notificacionproblema
                    ADD COLUMN IF NOT EXISTS motivo TEXT;
                """)
            else:
                # SQLite
                cursor.execute("""
                    PRAGMA table_info(notificacionproblema);
                """)
                columns = [col[1] for col in cursor.fetchall()]
                if 'motivo' not in columns:
                    cursor.execute("""
                        ALTER TABLE notificacionproblema
                        ADD COLUMN motivo TEXT;
                    """)
        except:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0055_add_fecha_vencimiento_to_pedido'),
    ]

    operations = [
        migrations.RunPython(add_motivo_field, migrations.RunPython.noop),
    ]
