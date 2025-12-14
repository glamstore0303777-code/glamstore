# Generated migration - add fields to NotificacionProblema

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0010_notificacionproblema_delete_notificacion'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificacionproblema',
            name='respuesta_admin',
            field=models.TextField(blank=True, db_column='respuesta_admin', null=True),
        ),
        migrations.AddField(
            model_name='notificacionproblema',
            name='fecha_respuesta',
            field=models.DateTimeField(blank=True, db_column='fecha_respuesta', null=True),
        ),
    ]
