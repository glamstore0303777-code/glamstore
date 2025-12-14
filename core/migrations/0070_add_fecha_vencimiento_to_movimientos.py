# Generated migration to add fecha_vencimiento field to MovimientoProducto

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0069_add_correo_pendiente_model'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimientoproducto',
            name='fecha_vencimiento',
            field=models.DateField(blank=True, db_column='fecha_vencimiento', help_text='Fecha de vencimiento del lote', null=True),
        ),
    ]
