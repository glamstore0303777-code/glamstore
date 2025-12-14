from django.db import migrations, models

class Migration(migrations.Migration):

    dependencies = [
        ('core', '0057_no_changes'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            ALTER TABLE pedidos
            ADD COLUMN IF NOT EXISTS fecha_vencimiento DATE;
            """,
            reverse_sql="""
            ALTER TABLE pedidos
            DROP COLUMN IF EXISTS fecha_vencimiento;
            """
        ),
    ]
