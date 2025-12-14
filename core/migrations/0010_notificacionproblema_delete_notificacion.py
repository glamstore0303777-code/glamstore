# Generated migration - create NotificacionProblema model

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0009_movimientoproducto_costo_unitario'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificacionProblema',
            fields=[
                ('idNotificacion', models.AutoField(db_column='idnotificacion', primary_key=True, serialize=False)),
                ('motivo', models.TextField(db_column='motivo')),
                ('foto', models.ImageField(blank=True, db_column='foto', null=True, upload_to='problemas_entrega/')),
                ('fechaReporte', models.DateTimeField(auto_now_add=True, db_column='fechareporte')),
                ('leida', models.BooleanField(db_column='leida', default=False)),
                ('idPedido', models.ForeignKey(db_column='idpedido', on_delete=django.db.models.deletion.CASCADE, to='core.pedido')),
            ],
            options={
                'db_table': 'notificaciones_problema',
                'app_label': 'core',
                'ordering': ['-fechaReporte'],
            },
        ),
    ]
