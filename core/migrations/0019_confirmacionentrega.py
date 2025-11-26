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
                ('idConfirmacion', models.AutoField(primary_key=True, serialize=False)),
                ('foto_entrega', models.ImageField(blank=True, null=True, upload_to='confirmaciones_entrega/')),
                ('calificacion', models.IntegerField(choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], default=5)),
                ('comentario', models.TextField(blank=True, null=True)),
                ('fecha_confirmacion', models.DateTimeField(auto_now_add=True)),
                ('pedido', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='confirmacion_entrega', to='core.pedido')),
                ('repartidor', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.repartidor')),
            ],
            options={
                'db_table': 'confirmaciones_entrega',
            },
        ),
    ]
