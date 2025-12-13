# Generated migration to create notificaciones tables for SQLite

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0043_populate_distribuidores'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            CREATE TABLE IF NOT EXISTS notificaciones_problema (
                "idNotificacion" INTEGER PRIMARY KEY AUTOINCREMENT,
                "idPedido" integer NOT NULL,
                "motivo" text NOT NULL,
                "foto" varchar(255) NULL,
                "fechaReporte" timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
                "leida" boolean NOT NULL DEFAULT 0,
                "respuesta_admin" text NULL,
                "fecha_respuesta" timestamp NULL
            );
            """,
            reverse_sql="DROP TABLE IF EXISTS notificaciones_problema;",
            state_operations=[]
        ),
        migrations.RunSQL(
            sql="""
            CREATE TABLE IF NOT EXISTS notificaciones_reporte (
                "idNotificacion" INTEGER PRIMARY KEY AUTOINCREMENT,
                "titulo" varchar(255) NOT NULL,
                "contenido_html" text NOT NULL,
                "tipo" varchar(50) NOT NULL DEFAULT 'DASHBOARD',
                "fechaCreacion" timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
                "leida" boolean NOT NULL DEFAULT 0
            );
            """,
            reverse_sql="DROP TABLE IF EXISTS notificaciones_reporte;",
            state_operations=[]
        ),
        migrations.RunSQL(
            sql="""
            CREATE TABLE IF NOT EXISTS mensajes_contacto (
                "idMensaje" INTEGER PRIMARY KEY AUTOINCREMENT,
                "nombre" varchar(50) NOT NULL,
                "email" varchar(100) NOT NULL,
                "asunto" varchar(100) NOT NULL,
                "mensaje" text NOT NULL,
                "fecha" timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
                "leido" boolean NOT NULL DEFAULT 0
            );
            """,
            reverse_sql="DROP TABLE IF EXISTS mensajes_contacto;",
            state_operations=[]
        ),
    ]
