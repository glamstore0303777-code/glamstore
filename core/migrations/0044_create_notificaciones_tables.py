# Generated migration to create notificaciones tables for PostgreSQL

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0043_populate_distribuidores'),
    ]

    operations = [
        migrations.RunSQL(
            sql="""
            CREATE TABLE IF NOT EXISTS notificaciones_problema (
                "idNotificacion" SERIAL PRIMARY KEY,
                "idPedido" integer NOT NULL,
                "motivo" text NOT NULL,
                "foto" varchar(255) NULL,
                "fechaReporte" timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
                "leida" boolean NOT NULL DEFAULT false,
                "respuesta_admin" text NULL,
                "fecha_respuesta" timestamp NULL
            );
            """,
            reverse_sql="DROP TABLE IF EXISTS notificaciones_problema CASCADE;",
            state_operations=[]
        ),
        migrations.RunSQL(
            sql="""
            CREATE TABLE IF NOT EXISTS notificaciones_reporte (
                "idNotificacion" SERIAL PRIMARY KEY,
                "titulo" varchar(255) NOT NULL,
                "contenido_html" text NOT NULL,
                "tipo" varchar(50) NOT NULL DEFAULT 'DASHBOARD',
                "fechaCreacion" timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
                "leida" boolean NOT NULL DEFAULT false
            );
            """,
            reverse_sql="DROP TABLE IF EXISTS notificaciones_reporte CASCADE;",
            state_operations=[]
        ),
        migrations.RunSQL(
            sql="""
            CREATE TABLE IF NOT EXISTS mensajes_contacto (
                "idMensaje" SERIAL PRIMARY KEY,
                "nombre" varchar(50) NOT NULL,
                "email" varchar(100) NOT NULL,
                "asunto" varchar(100) NOT NULL,
                "mensaje" text NOT NULL,
                "fecha" timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
                "leido" boolean NOT NULL DEFAULT false
            );
            """,
            reverse_sql="DROP TABLE IF EXISTS mensajes_contacto CASCADE;",
            state_operations=[]
        ),
    ]
