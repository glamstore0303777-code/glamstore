from django.db import migrations

def add_missing_columns(apps, schema_editor):
    """Agregar columnas faltantes a la tabla pedidos"""
    from django.db import connection
    
    with connection.cursor() as cursor:
        # Agregar columna estado_pago si no existe
        cursor.execute("""
            ALTER TABLE pedidos
            ADD COLUMN IF NOT EXISTS estado_pago VARCHAR(20) DEFAULT 'Pago Completo'
        """)
        
        # Agregar columna estado_pedido si no existe
        cursor.execute("""
            ALTER TABLE pedidos
            ADD COLUMN IF NOT EXISTS estado_pedido VARCHAR(20) DEFAULT 'Pedido Recibido'
        """)

def reverse_columns(apps, schema_editor):
    """Revertir cambios"""
    pass

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0054_create_missing_tables_final'),
    ]

    operations = [
        migrations.RunPython(add_missing_columns, reverse_columns),
    ]
