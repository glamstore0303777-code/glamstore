# Generated migration to fix movimientos_lote.lote_id column

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0084_fix_movimientos_decimal_fields'),
    ]

    operations = [
        # Paso 1: Crear la columna lote_id si no existe
        migrations.RunSQL(
            sql="""
            DO $$ 
            BEGIN
                IF NOT EXISTS (
                    SELECT 1 FROM information_schema.columns 
                    WHERE table_name = 'movimientos_lote' AND column_name = 'lote_id'
                ) THEN
                    ALTER TABLE movimientos_lote ADD COLUMN lote_id INTEGER;
                END IF;
            END $$;
            """,
            reverse_sql="-- Reverse not needed"
        ),
        
        # Paso 2: Copiar datos de idlote a lote_id si existen
        migrations.RunSQL(
            sql="""
            UPDATE movimientos_lote 
            SET lote_id = idlote 
            WHERE lote_id IS NULL AND idlote IS NOT NULL;
            """,
            reverse_sql="-- Reverse not needed"
        ),
        
        # Paso 3: Eliminar constraint anterior si existe
        migrations.RunSQL(
            sql="""
            DO $$ 
            BEGIN
                IF EXISTS (
                    SELECT 1 FROM information_schema.table_constraints 
                    WHERE table_name = 'movimientos_lote' AND constraint_name = 'movimientos_lote_lote_id_fkey'
                ) THEN
                    ALTER TABLE movimientos_lote DROP CONSTRAINT movimientos_lote_lote_id_fkey;
                END IF;
            END $$;
            """,
            reverse_sql="-- Reverse not needed"
        ),
        
        # Paso 4: Agregar la foreign key constraint
        migrations.RunSQL(
            sql="""
            DO $$ 
            BEGIN
                IF NOT EXISTS (
                    SELECT 1 FROM information_schema.table_constraints 
                    WHERE table_name = 'movimientos_lote' AND constraint_name = 'movimientos_lote_lote_id_fkey'
                ) THEN
                    ALTER TABLE movimientos_lote 
                    ADD CONSTRAINT movimientos_lote_lote_id_fkey 
                    FOREIGN KEY (lote_id) REFERENCES lotes_producto(idlote) ON DELETE CASCADE;
                END IF;
            END $$;
            """,
            reverse_sql="-- Reverse not needed"
        ),
    ]
