# Generated migration - fix Cliente model to match current definition

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0036_add_missing_pedido_fields'),
    ]

    operations = [
        # Remove old fields from Cliente
        migrations.RemoveField(
            model_name='cliente',
            name='nombreCliente',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='apellidoCliente',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='emailCliente',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='telefonoCliente',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='direccionCliente',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='ciudadCliente',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='departamentoCliente',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='codigoPostalCliente',
        ),
        migrations.RemoveField(
            model_name='cliente',
            name='usuario',
        ),
        # Add new fields to Cliente
        migrations.AddField(
            model_name='cliente',
            name='cedula',
            field=models.CharField(db_column='cedula', max_length=20, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='nombre',
            field=models.CharField(db_column='nombre', max_length=100, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='email',
            field=models.CharField(db_column='email', max_length=100, unique=True, default=''),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='cliente',
            name='direccion',
            field=models.CharField(db_column='direccion', max_length=200, null=True),
            preserve_default=True,
        ),
        migrations.AddField(
            model_name='cliente',
            name='telefono',
            field=models.CharField(db_column='telefono', max_length=20, null=True),
            preserve_default=True,
        ),
    ]
