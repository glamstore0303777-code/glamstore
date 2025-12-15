# Generated migration to ensure notificaciones_problema table exists

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0080_add_proveedor_to_lotes'),
    ]

    operations = [
        migrations.CreateModel(
            name='NotificacionProblema',
            fields=[
                ('idNotificacion', models.AutoField(db_column='idnotificacion', primary_key=True, serialize=False)),
                ('motivo', models.TextField(blank=True, db_column='motivo', null=True)),
                ('foto', models.ImageField(blank=True, db_column='foto', null=True, upload_to='problemas_entrega/')),
                ('fechaReporte', models.DateTimeField(auto_now_add=True, db_column='fechareporte')),
                ('leida', models.BooleanField(db_column='leida', default=False)),
                ('respuesta_admin', models.TextField(blank=True, db_column='respuesta_admin', null=True)),
                ('fecha_respuesta', models.DateTimeField(blank=True, db_column='fecha_respuesta', null=True)),
                ('idPedido', models.ForeignKey(db_column='idpedido', on_delete=django.db.models.deletion.CASCADE, to='core.pedido')),
            ],
            options={
                'db_table': 'notificaciones_problema',
                'managed': True,
            },
        ),
    ]
