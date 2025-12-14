"""
Migration to fix ALL column case sensitivity issues across ALL tables.
"""
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0048_fix_all_column_cases'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                DO $$
                DECLARE
                    col_record RECORD;
                    tbl_record RECORD;
                BEGIN
                    -- Loop through all relevant tables
                    FOR tbl_record IN 
                        SELECT tablename FROM pg_tables 
                        WHERE schemaname = 'public' 
                        AND tablename IN ('productos', 'categorias', 'subcategorias', 
                                          'pedidos', 'detallepedido', 'clientes', 
                                          'repartidores', 'usuarios', 'distribuidores',
                                          'pedidoproducto', 'movimientoproducto')
                    LOOP
                        -- For each table, check all columns
                        FOR col_record IN 
                            SELECT attname 
                            FROM pg_attribute 
                            WHERE attrelid = tbl_record.tablename::regclass 
                            AND attnum > 0 
                            AND NOT attisdropped
                            AND attname ~ '[A-Z]'  -- Only columns with uppercase letters
                        LOOP
                            -- Rename column to lowercase
                            BEGIN
                                EXECUTE format('ALTER TABLE %I RENAME COLUMN %I TO %I', 
                                    tbl_record.tablename, 
                                    col_record.attname, 
                                    lower(col_record.attname));
                                RAISE NOTICE 'Renamed %.% to %', tbl_record.tablename, col_record.attname, lower(col_record.attname);
                            EXCEPTION WHEN OTHERS THEN
                                RAISE NOTICE 'Could not rename %.%: %', tbl_record.tablename, col_record.attname, SQLERRM;
                            END;
                        END LOOP;
                    END LOOP;
                END $$;
            """,
            reverse_sql="SELECT 1;",
        ),
    ]
