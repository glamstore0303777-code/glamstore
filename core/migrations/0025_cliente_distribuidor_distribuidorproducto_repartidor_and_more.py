# Generated migration - create additional models

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0024_producto_precio_venta'),
    ]

    operations = [
        migrations.CreateModel(
            name='Distribuidor',
            fields=[
                ('idDistribuidor', models.AutoField(primary_key=True, serialize=False)),
                ('nombreDistribuidor', models.CharField(max_length=30, null=True, db_column='nombredistribuidor')),
                ('contacto', models.CharField(max_length=20, db_column='contacto')),
            ],
            options={
                'db_table': 'distribuidores',
                'managed': False,
                'app_label': 'core',
            },
        ),
        migrations.CreateModel(
            name='DistribuidorProducto',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('idDistribuidor', models.IntegerField(db_column='iddistribuidor')),
                ('idProducto', models.CharField(max_length=30, db_column='idproducto')),
            ],
            options={
                'db_table': 'distribuidor_producto',
                'managed': False,
                'app_label': 'core',
            },
        ),
    ]
