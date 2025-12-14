"""
Migration to ensure configuracion_global table exists and fix any remaining column issues.
"""
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0049_fix_all_tables_columns'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
                -- Create configuracion_global table if not exists
                CREATE TABLE IF NOT EXISTS configuracion_global (
                    id BIGSERIAL PRIMARY KEY,
                    margen_ganancia DECIMAL(5,2) DEFAULT 10,
                    fecha_actualizacion TIMESTAMP DEFAULT NOW()
                );
                
                -- Insert default config if empty
                INSERT INTO configuracion_global (id, margen_ganancia, fecha_actualizacion)
                VALUES (1, 10, NOW())
                ON CONFLICT (id) DO NOTHING;
                
                -- Fix any remaining camelCase columns in ALL tables
                DO $$
                DECLARE
                    col_record RECORD;
                    tbl_record RECORD;
                BEGIN
                    FOR tbl_record IN 
                        SELECT tablename FROM pg_tables 
                        WHERE schemaname = 'public'
                    LOOP
                        FOR col_record IN 
                            SELECT attname 
                            FROM pg_attribute 
                            WHERE attrelid = tbl_record.tablename::regclass 
                            AND attnum > 0 
                            AND NOT attisdropped
                            AND attname ~ '[A-Z]'
                        LOOP
                            BEGIN
                                EXECUTE format('ALTER TABLE %I RENAME COLUMN %I TO %I', 
                                    tbl_record.tablename, 
                                    col_record.attname, 
                                    lower(col_record.attname));
                            EXCEPTION WHEN OTHERS THEN
                                NULL;
                            END;
                        END LOOP;
                    END LOOP;
                END $$;
            """,
            reverse_sql="SELECT 1;",
        ),
    ]
