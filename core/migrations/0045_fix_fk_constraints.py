"""
Migration to fix FK constraints pointing to wrong table names
"""
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_fix_column_case_sensitivity'),
    ]

    operations = [
        # Drop old FK constraints that point to wrong table names
        migrations.RunSQL(
            sql="""
            DO $$
            BEGIN
                -- Drop FK constraint on productos.idcategoria if it exists
                IF EXISTS (
                    SELECT 1 FROM information_schema.table_constraints 
                    WHERE constraint_name = 'productos_idCategoria_e28f49a8_fk_categoria_idCategoria'
                ) THEN
                    ALTER TABLE productos DROP CONSTRAINT "productos_idCategoria_e28f49a8_fk_categoria_idCategoria";
                END IF;
                
                -- Drop any other FK constraints with wrong table references
                IF EXISTS (
                    SELECT 1 FROM information_schema.table_constraints 
                    WHERE constraint_name LIKE '%fk_categoria_%' AND table_name = 'productos'
                ) THEN
                    -- Get and drop all such constraints
                    EXECUTE (
                        SELECT string_agg('ALTER TABLE productos DROP CONSTRAINT "' || constraint_name || '"', '; ')
                        FROM information_schema.table_constraints 
                        WHERE constraint_name LIKE '%fk_categoria_%' AND table_name = 'productos'
                    );
                END IF;
                
                -- Drop FK constraint on productos.idsubcategoria if wrong
                IF EXISTS (
                    SELECT 1 FROM information_schema.table_constraints 
                    WHERE constraint_name LIKE '%fk_subcategoria_%' AND table_name = 'productos'
                ) THEN
                    EXECUTE (
                        SELECT string_agg('ALTER TABLE productos DROP CONSTRAINT "' || constraint_name || '"', '; ')
                        FROM information_schema.table_constraints 
                        WHERE constraint_name LIKE '%fk_subcategoria_%' AND table_name = 'productos'
                    );
                END IF;
            END $$;
            """,
            reverse_sql=migrations.RunSQL.noop,
        ),
    ]
