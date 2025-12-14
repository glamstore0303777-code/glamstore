"""
Migration to drop subcategoria FK constraint
"""
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0045_fix_fk_constraints'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            DO $$
            DECLARE
                r RECORD;
            BEGIN
                -- Drop ALL FK constraints on productos table
                FOR r IN (
                    SELECT constraint_name 
                    FROM information_schema.table_constraints 
                    WHERE table_name = 'productos' 
                    AND constraint_type = 'FOREIGN KEY'
                ) LOOP
                    EXECUTE 'ALTER TABLE productos DROP CONSTRAINT IF EXISTS "' || r.constraint_name || '"';
                END LOOP;
            END $$;
            """,
            reverse_sql=migrations.RunSQL.noop,
        ),
    ]
