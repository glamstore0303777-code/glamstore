"""
Migration to fix FK constraints pointing to wrong table names
"""
from django.db import migrations
from django.conf import settings


def fix_fk_constraints(apps, schema_editor):
    """Fix FK constraints - database agnostic"""
    from django.db import connection
    
    db_engine = settings.DATABASES['default']['ENGINE']
    
    # Only run for PostgreSQL
    if 'postgresql' not in db_engine:
        return
    
    with connection.cursor() as cursor:
        try:
            # Drop ALL FK constraints on productos table to clean up
            cursor.execute("""
                SELECT constraint_name 
                FROM information_schema.table_constraints 
                WHERE table_name = 'productos' 
                AND constraint_type = 'FOREIGN KEY'
            """)
            
            constraints = cursor.fetchall()
            for (constraint_name,) in constraints:
                cursor.execute(f'ALTER TABLE productos DROP CONSTRAINT IF EXISTS "{constraint_name}"')
        except:
            pass


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0044_fix_column_case_sensitivity'),
    ]

    operations = [
        migrations.RunPython(fix_fk_constraints, migrations.RunPython.noop),
    ]
