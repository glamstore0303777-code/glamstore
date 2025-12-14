"""
Migration to add fechacreacion column to pedidos table if it doesn't exist.
"""
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0050_ensure_configuracion_table'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                -- Add fechacreacion column if it doesn't exist
                DO $$
                BEGIN
                    -- Check if column exists (any case)
                    IF NOT EXISTS (
                        SELECT 1 FROM pg_attribute 
                        WHERE attrelid = 'pedidos'::regclass 
                        AND attnum > 0 
                        AND NOT attisdropped
                        AND lower(attname) = 'fechacreacion'
                    ) THEN
                        -- Add the column
                        ALTER TABLE pedidos ADD COLUMN fechacreacion TIMESTAMP DEFAULT NOW();
                    END IF;
                    
                    -- Try to rename if it exists with different case
                    BEGIN
                        ALTER TABLE pedidos RENAME COLUMN "fechaCreacion" TO fechacreacion;
                    EXCEPTION WHEN OTHERS THEN
                        NULL;
                    END;
                    
                    BEGIN
                        ALTER TABLE pedidos RENAME COLUMN "FechaCreacion" TO fechacreacion;
                    EXCEPTION WHEN OTHERS THEN
                        NULL;
                    END;
                    
                    BEGIN
                        ALTER TABLE pedidos RENAME COLUMN "fecha_creacion" TO fechacreacion;
                    EXCEPTION WHEN OTHERS THEN
                        NULL;
                    END;
                END $$;
            """,
            reverse_sql="SELECT 1;",
        ),
    ]
