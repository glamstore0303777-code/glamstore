# Generated migration - fecha_vencimiento column already exists in database

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0054_create_missing_tables_final'),
    ]

    operations = [
        migrations.AddField(
            model_name='pedido',
            name='fecha_vencimiento',
            field=models.DateField(null=True, blank=True, db_column='fecha_vencimiento'),
        ),
    ]
