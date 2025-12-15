# Generated migration to ensure mensajes_contacto table exists

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0081_ensure_notificaciones_problema_table'),
    ]

    operations = [
        migrations.CreateModel(
            name='MensajeContacto',
            fields=[
                ('idMensaje', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=100)),
                ('mensaje', models.TextField()),
                ('fecha', models.DateTimeField(auto_now_add=True)),
            ],
            options={
                'db_table': 'mensajes_contacto',
                'managed': False,
            },
        ),
    ]
