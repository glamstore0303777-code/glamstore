# Generated migration to add missing columns to notificaciones_problema

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0076_fix_duplicate_columns'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            CREATE TABLE IF NOT EXISTS notificaciones_problema_new (
                idnotificacion INTEGER PRIMARY KEY AUTOINCREMENT,
                idpedido BIGINT NOT NULL,
                motivo TEXT,
                foto VARCHAR(100),
                fechareporte DATETIME DEFAULT CURRENT_TIMESTAMP,
                leida BOOLEAN DEFAULT 0,
                respuesta_admin TEXT,
                fecha_respuesta DATETIME,
                FOREIGN KEY (idpedido) REFERENCES pedidos(idpedido)
            );
            
            INSERT INTO notificaciones_problema_new 
            SELECT 
                idnotificacion,
                idpedido,
                motivo,
                foto,
                COALESCE(fechareporte, CURRENT_TIMESTAMP),
                leida,
                respuesta_admin,
                fecha_respuesta
            FROM notificaciones_problema;
            
            DROP TABLE notificaciones_problema;
            
            ALTER TABLE notificaciones_problema_new RENAME TO notificaciones_problema;
            """,
            reverse_sql="",
        ),
    ]
