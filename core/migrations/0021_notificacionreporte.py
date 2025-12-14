# Generated migration - create NotificacionReporte model

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0020_loteproducto_movimientolote_and_more'),
    ]

    operations = [
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
    ]
