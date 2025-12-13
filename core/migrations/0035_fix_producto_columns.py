# Generated migration - fix Producto column names

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0034_fix_table_names'),
    ]

    operations = [
        # Rename columns in productos table to match model db_column definitions
        migrations.RunSQL(
            sql="""
            BEGIN;
            -- This is a no-op for now as the columns should already exist
            -- If needed, specific column renames can be added here
            COMMIT;
            """,
            reverse_sql="SELECT 1;",
            state_operations=[],
        ),
    ]
