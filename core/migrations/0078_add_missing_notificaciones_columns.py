# Generated migration to add missing columns to notificaciones_problema

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0076_fix_duplicate_columns'),
    ]

    operations = [
        migrations.AddField(
            model_name='notificacionproblema',
            name='fechaReporte',
            field=models.DateTimeField(auto_now_add=True, db_column='fechareporte', default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
