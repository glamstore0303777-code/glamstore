# Generated migration - create ConfirmacionEntrega model

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0018_add_missing_movimientos_columns'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfirmacionEntrega',
            fields=[
                ('idConfirmacion', models.AutoField(db_column='idconfirmacion', primary_key=True, serialize=False)),
                ('foto_entrega', models.ImageField(blank=True, db_column='foto_entrega', null=True, upload_to='confirmaciones_entrega/')),
                ('calificacion', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], db_column='calificacion', default=5)),
                ('comentario', models.TextField(blank=True, db_column='comentario', null=True)),
                ('fecha_confirmacion', models.DateTimeField(auto_now_add=True, db_column='fecha_confirmacion')),
                ('pedido', models.OneToOneField(db_column='pedido_id', on_delete=django.db.models.deletion.CASCADE, related_name='confirmacion_entrega', to='core.pedido')),
                ('repartidor', models.ForeignKey(blank=True, db_column='repartidor_id', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.repartidor')),
            ],
            options={
                'db_table': 'confirmaciones_entrega',
                'app_label': 'core',
            },
        ),
    ]
