# Generated migration - create all models based on current model definitions

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0029_detallepedido_margen_ganancia'),
    ]

    operations = [
        # Create MovimientoProducto
        migrations.CreateModel(
            name='MovimientoProducto',
            fields=[
                ('idMovimiento', models.AutoField(db_column='idmovimiento', primary_key=True, serialize=False)),
                ('fecha', models.DateTimeField(auto_now_add=True, db_column='fecha')),
                ('tipo_movimiento', models.CharField(choices=[('ENTRADA_INICIAL', 'Entrada Inicial'), ('AJUSTE_MANUAL_ENTRADA', 'Ajuste Manual (Entrada)'), ('AJUSTE_MANUAL_SALIDA', 'Ajuste Manual (Salida)'), ('SALIDA_VENTA', 'Salida por Venta'), ('EN_PREPARACION_SALIDA', 'En Preparación (Apartado)'), ('PERDIDA_VENCIMIENTO', 'Pérdida por Vencimiento')], db_column='tipo_movimiento', max_length=50)),
                ('cantidad', models.IntegerField(db_column='cantidad')),
                ('precio_unitario', models.DecimalField(db_column='precio_unitario', decimal_places=2, default=0, max_digits=10)),
                ('costo_unitario', models.DecimalField(db_column='costo_unitario', decimal_places=2, default=0, help_text='Costo por unidad para movimientos de entrada.', max_digits=10)),
                ('stock_anterior', models.IntegerField(db_column='stock_anterior')),
                ('stock_nuevo', models.IntegerField(db_column='stock_nuevo')),
                ('descripcion', models.CharField(blank=True, db_column='descripcion', max_length=255, null=True)),
                ('lote', models.CharField(blank=True, db_column='lote', help_text='Código del lote del producto', max_length=100, null=True)),
                ('fecha_vencimiento', models.DateField(blank=True, db_column='fecha_vencimiento', help_text='Fecha de vencimiento del producto', null=True)),
                ('total_con_iva', models.DecimalField(blank=True, db_column='total_con_iva', decimal_places=2, help_text='Total incluyendo IVA', max_digits=10, null=True)),
                ('iva', models.DecimalField(blank=True, db_column='iva', decimal_places=2, help_text='Valor del IVA (19%)', max_digits=10, null=True)),
                ('id_pedido', models.ForeignKey(blank=True, db_column='idpedido', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.pedido')),
                ('producto', models.ForeignKey(db_column='producto_id', on_delete=django.db.models.deletion.CASCADE, related_name='movimientos', to='core.producto')),
            ],
            options={
                'db_table': 'movimientos_producto',
                'app_label': 'core',
                'ordering': ['-fecha'],
            },
        ),
        # Create LoteProducto
        migrations.CreateModel(
            name='LoteProducto',
            fields=[
                ('idLote', models.AutoField(db_column='idlote', primary_key=True, serialize=False)),
                ('codigo_lote', models.CharField(db_column='codigo_lote', help_text='Código único del lote', max_length=100)),
                ('fecha_entrada', models.DateTimeField(auto_now_add=True, db_column='fecha_entrada')),
                ('fecha_vencimiento', models.DateField(blank=True, db_column='fecha_vencimiento', null=True)),
                ('cantidad_inicial', models.IntegerField(db_column='cantidad_inicial', help_text='Cantidad inicial del lote')),
                ('cantidad_disponible', models.IntegerField(db_column='cantidad_disponible', help_text='Cantidad disponible actual')),
                ('costo_unitario', models.DecimalField(db_column='costo_unitario', decimal_places=2, default=0, max_digits=10)),
                ('precio_venta', models.DecimalField(db_column='precio_venta', decimal_places=2, default=0, max_digits=10)),
                ('total_con_iva', models.DecimalField(blank=True, db_column='total_con_iva', decimal_places=2, max_digits=10, null=True)),
                ('iva', models.DecimalField(blank=True, db_column='iva', decimal_places=2, max_digits=10, null=True)),
                ('proveedor', models.CharField(blank=True, db_column='proveedor', max_length=200, null=True)),
                ('producto', models.ForeignKey(db_column='producto_id', on_delete=django.db.models.deletion.CASCADE, related_name='lotes', to='core.producto')),
            ],
            options={
                'db_table': 'lotes_producto',
                'app_label': 'core',
                'ordering': ['fecha_entrada'],
                'unique_together': {('producto', 'codigo_lote')},
            },
        ),
        # Create MovimientoLote
        migrations.CreateModel(
            name='MovimientoLote',
            fields=[
                ('idMovimientoLote', models.AutoField(db_column='idmovimientolote', primary_key=True, serialize=False)),
                ('cantidad', models.IntegerField(db_column='cantidad', help_text='Cantidad tomada de este lote')),
                ('fecha', models.DateTimeField(auto_now_add=True, db_column='fecha')),
                ('lote', models.ForeignKey(db_column='lote_id', on_delete=django.db.models.deletion.CASCADE, related_name='movimientos', to='core.loteproducto')),
                ('movimiento_producto', models.ForeignKey(db_column='movimiento_producto_id', on_delete=django.db.models.deletion.CASCADE, related_name='movimientos_lote', to='core.movimientoproducto')),
            ],
            options={
                'db_table': 'movimientos_lote',
                'app_label': 'core',
                'ordering': ['-fecha'],
            },
        ),
        # Add lote_origen field to MovimientoProducto
        migrations.AddField(
            model_name='movimientoproducto',
            name='lote_origen',
            field=models.ForeignKey(blank=True, db_column='lote_origen_id', help_text='Lote del cual salió el producto (para movimientos de salida)', null=True, on_delete=django.db.models.deletion.SET_NULL, to='core.loteproducto'),
        ),
        # Create ConfiguracionGlobal
        migrations.CreateModel(
            name='ConfiguracionGlobal',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('margen_ganancia', models.DecimalField(db_column='margen_ganancia', decimal_places=2, default=10, help_text='Porcentaje de ganancia global para todos los productos (ej: 10 para 10%)', max_digits=5)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, db_column='fecha_actualizacion')),
            ],
            options={
                'db_table': 'configuracion_global',
                'app_label': 'core',
                'verbose_name': 'Configuración Global',
                'verbose_name_plural': 'Configuración Global',
            },
        ),
        # Create NotificacionProblema
        migrations.CreateModel(
            name='NotificacionProblema',
            fields=[
                ('idNotificacion', models.AutoField(db_column='idnotificacion', primary_key=True, serialize=False)),
                ('motivo', models.TextField(db_column='motivo')),
                ('foto', models.ImageField(blank=True, db_column='foto', null=True, upload_to='problemas_entrega/')),
                ('fechaReporte', models.DateTimeField(auto_now_add=True, db_column='fechareporte')),
                ('leida', models.BooleanField(db_column='leida', default=False)),
                ('respuesta_admin', models.TextField(blank=True, db_column='respuesta_admin', null=True)),
                ('fecha_respuesta', models.DateTimeField(blank=True, db_column='fecha_respuesta', null=True)),
                ('idPedido', models.ForeignKey(db_column='idpedido', on_delete=django.db.models.deletion.CASCADE, to='core.pedido')),
            ],
            options={
                'db_table': 'notificaciones_problema',
                'app_label': 'core',
                'ordering': ['-fechaReporte'],
            },
        ),
        # Create NotificacionReporte
        migrations.CreateModel(
            name='NotificacionReporte',
            fields=[
                ('idNotificacion', models.AutoField(db_column='idnotificacion', primary_key=True, serialize=False)),
                ('titulo', models.CharField(db_column='titulo', max_length=255)),
                ('contenido_html', models.TextField(db_column='contenido_html')),
                ('tipo', models.CharField(db_column='tipo', default='DASHBOARD', max_length=50)),
                ('fechaCreacion', models.DateTimeField(auto_now_add=True, db_column='fechacreacion')),
                ('leida', models.BooleanField(db_column='leida', default=False)),
            ],
            options={
                'db_table': 'notificaciones_reporte',
                'app_label': 'core',
                'ordering': ['-fechaCreacion'],
            },
        ),
        # Create ConfirmacionEntrega
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
        # Create ImagenProducto
        migrations.CreateModel(
            name='ImagenProducto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idProducto', models.BigIntegerField(db_column='id_producto')),
                ('nombreArchivo', models.CharField(db_column='nombre_archivo', max_length=255)),
                ('ruta', models.CharField(db_column='ruta', max_length=255)),
                ('contenido', models.BinaryField(db_column='contenido')),
                ('fechaSubida', models.DateTimeField(auto_now_add=True, db_column='fecha_subida')),
            ],
            options={
                'db_table': 'imagenes_productos',
                'app_label': 'core',
            },
        ),
        # Create ImagenCategoria
        migrations.CreateModel(
            name='ImagenCategoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idCategoria', models.IntegerField(db_column='id_categoria')),
                ('nombreArchivo', models.CharField(db_column='nombre_archivo', max_length=255)),
                ('ruta', models.CharField(db_column='ruta', max_length=255)),
                ('contenido', models.BinaryField(db_column='contenido')),
                ('fechaSubida', models.DateTimeField(auto_now_add=True, db_column='fecha_subida')),
            ],
            options={
                'db_table': 'imagenes_categorias',
                'app_label': 'core',
            },
        ),
        # Create CorreoPendiente
        migrations.CreateModel(
            name='CorreoPendiente',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('idPedido', models.IntegerField(db_column='id_pedido')),
                ('destinatario', models.CharField(db_column='destinatario', max_length=255)),
                ('asunto', models.CharField(db_column='asunto', max_length=255)),
                ('contenido_html', models.TextField(db_column='contenido_html')),
                ('contenido_texto', models.TextField(db_column='contenido_texto')),
                ('enviado', models.BooleanField(db_column='enviado', default=False)),
                ('intentos', models.IntegerField(db_column='intentos', default=0)),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True, db_column='fecha_creacion')),
                ('fecha_envio', models.DateTimeField(blank=True, db_column='fecha_envio', null=True)),
                ('error', models.TextField(blank=True, db_column='error', null=True)),
            ],
            options={
                'db_table': 'correos_pendientes',
                'app_label': 'core',
            },
        ),
    ]
