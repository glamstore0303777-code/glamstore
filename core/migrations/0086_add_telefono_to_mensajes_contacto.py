# Generated migration to add telefono column to mensajes_contacto

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0085_fix_movimientos_lote_column'),
    ]

    operations = [
        # Agregar la columna telefono si no existe
        migrations.RunSQL(
            sql="""
            DO $$ 
            BEGIN
                IF NOT EXISTS (
                    SELECT 1 FROM information_schema.columns 
                    WHERE table_name = 'mensajes_contacto' AND column_name = 'telefono'
                ) THEN
                    ALTER TABLE mensajes_contacto ADD COLUMN telefono VARCHAR(20);
                END IF;
            END $$;
            """,
            reverse_sql="-- Reverse not needed"
        ),
    ]
