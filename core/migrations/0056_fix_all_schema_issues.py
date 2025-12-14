from django.db import migrations

def fix_schema_issues(apps, schema_editor):
    """
    Fix all database schema issues:
    1. Add producto_id column to lotes_producto table
    2. Ensure estado_pago column exists in pedidos table
    3. Create mensajes_contacto table if it doesn't exist
    """
    from django.db import connection
    
    with connection.cursor() as cursor:
        # 1. Add producto_id column to lotes_producto if it doesn't exist
        cursor.execute("""
            ALTER TABLE lotes_producto
            ADD COLUMN IF NOT EXISTS producto_id INTEGER
        """)
        
        # Add foreign key constraint if it doesn't exist
        cursor.execute("""
            ALTER TABLE lotes_producto
            ADD CONSTRAINT IF NOT EXISTS lotes_producto_producto_id_fk
            FOREIGN KEY (producto_id) REFERENCES productos(idproducto) ON DELETE CASCADE
        """)
        
        # 2. Ensure estado_pago column exists in pedidos table
        cursor.execute("""
            ALTER TABLE pedidos
            ADD COLUMN IF NOT EXISTS estado_pago VARCHAR(20) DEFAULT 'Pago Completo'
        """)
        
        # 3. Create mensajes_contacto table if it doesn't exist
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS mensajes_contacto (
                idmensaje SERIAL PRIMARY KEY,
                nombre VARCHAR(50) NOT NULL,
                email VARCHAR(100) NOT NULL,
                mensaje TEXT NOT NULL,
                fecha TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        """)

def reverse_schema_fixes(apps, schema_editor):
    """Revert schema changes"""
    from django.db import connection
    
    with connection.cursor() as cursor:
        # Drop foreign key constraint
        cursor.execute("""
            ALTER TABLE lotes_producto
            DROP CONSTRAINT IF EXISTS lotes_producto_producto_id_fk
        """)
        
        # Drop producto_id column
        cursor.execute("""
            ALTER TABLE lotes_producto
            DROP COLUMN IF EXISTS producto_id
        """)
        
        # Drop estado_pago column
        cursor.execute("""
            ALTER TABLE pedidos
            DROP COLUMN IF EXISTS estado_pago
        """)
        
        # Drop mensajes_contacto table
        cursor.execute("""
            DROP TABLE IF EXISTS mensajes_contacto CASCADE
        """)

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0055_add_missing_pedido_columns'),
    ]

    operations = [
        migrations.RunPython(fix_schema_issues, reverse_schema_fixes),
    ]
