# Generated migration to add proveedor field to lotes_producto

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0078_add_missing_notificaciones_columns'),
    ]

    operations = [
        migrations.AddField(
            model_name='loteproducto',
            name='proveedor',
            field=models.CharField(max_length=200, null=True, blank=True, db_column='proveedor'),
        ),
    ]
