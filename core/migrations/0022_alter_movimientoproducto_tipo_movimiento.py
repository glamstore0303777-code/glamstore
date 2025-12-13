# Generated migration - add lote_origen field to MovimientoProducto

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0021_notificacionreporte'),
    ]

    operations = [
        migrations.AddField(
            model_name='movimientoproducto',
            name='lote_origen',
            field=models.ForeignKey(blank=True, db_column='lote_origen_id', help_text='Lote del cual salió el producto (para movimientos de salida)', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.loteproducto'),
        ),
    ]
