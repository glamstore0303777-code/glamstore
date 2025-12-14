from django.db import migrations

def add_fecha_vencimiento_column(apps, schema_editor):
    """Agregar columna fecha_vencimiento a la tabla pedidos si no existe"""
    from django.db import connection
    
    with connection.cursor() as cursor:
        db_engine = connection.settings_dict['ENGINE']
        
        if 'postgresql' in db_engine:
            # PostgreSQL
            cursor.execute("""
                ALTER TABLE pedidos
                ADD COLUMN IF NOT EXISTS fecha_vencimiento DATE;
            """)
        elif 'sqlite' in db_engine:
            # SQLite
            cursor.execute("""
                PRAGMA table_info(pedidos);
            """)
            columns = [col[1] for col in cursor.fetchall()]
            if 'fecha_vencimiento' not in columns:
                cursor.execute("""
                    ALTER TABLE pedidos
                    ADD COLUMN fecha_vencimiento DATE;
                """)

def remove_fecha_vencimiento_column(apps, schema_editor):
    """Revertir la adición de la columna"""
    from django.db import connection
    
    with connection.cursor() as cursor:
        db_engine = connection.settings_dict['ENGINE']
        
        if 'postgresql' in db_engine:
            cursor.execute("""
                ALTER TABLE pedidos
                DROP COLUMN IF EXISTS fecha_vencimiento;
            """)

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0054_create_missing_tables_final'),
    ]

    operations = [
        migrations.RunPython(add_fecha_vencimiento_column, remove_fecha_vencimiento_column),
    ]
