# Generated migration to create configuracion_global table

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0032_create_all_tables'),
    ]

    operations = [
        migrations.CreateModel(
            name='ConfiguracionGlobal',
            fields=[
                ('id', models.BigAutoField(db_column='id', primary_key=True, serialize=False)),
                ('margen_ganancia', models.DecimalField(db_column='margen_ganancia', decimal_places=2, default=10, help_text='Porcentaje de ganancia global para todos los productos (ej: 10 para 10%)', max_digits=5)),
                ('fecha_actualizacion', models.DateTimeField(auto_now=True, db_column='fecha_actualizacion')),
            ],
            options={
                'verbose_name': 'Configuración Global',
                'verbose_name_plural': 'Configuración Global',
                'db_table': 'configuracion_global',
                'managed': False,
            },
        ),
    ]
