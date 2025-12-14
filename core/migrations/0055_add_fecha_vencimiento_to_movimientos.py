# Generated migration - add fecha_vencimiento to movimientos_producto table

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0054_create_missing_tables_final'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimientoproducto',
            name='fecha_vencimiento',
            field=models.DateField(blank=True, null=True, db_column='fecha_vencimiento', help_text='Fecha de vencimiento del producto'),
        ),
    ]
