# Generated migration to create notificaciones tables - compatible with PostgreSQL and SQLite

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0043_populate_distribuidores'),
    ]

    def create_notificaciones_tables(apps, schema_editor):
        """Create notificaciones tables - compatible with PostgreSQL and SQLite"""
        with schema_editor.connection.cursor() as cursor:
            db_vendor = schema_editor.connection.vendor
            
            if db_vendor == 'postgresql':
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS notificaciones_problema (
                        "idNotificacion" BIGSERIAL PRIMARY KEY,
                        "idPedido" BIGINT NOT NULL,
                        "motivo" text NOT NULL,
                        "foto" varchar(255) NULL,
                        "fechaReporte" timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
                        "leida" boolean NOT NULL DEFAULT FALSE,
                        "respuesta_admin" text NULL,
                        "fecha_respuesta" timestamp NULL
                    );
                """)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS notificaciones_reporte (
                        "idNotificacion" BIGSERIAL PRIMARY KEY,
                        "titulo" varchar(255) NOT NULL,
                        "contenido_html" text NOT NULL,
                        "tipo" varchar(50) NOT NULL DEFAULT 'DASHBOARD',
                        "fechaCreacion" timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
                        "leida" boolean NOT NULL DEFAULT FALSE
                    );
                """)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS mensajes_contacto (
                        "idMensaje" BIGSERIAL PRIMARY KEY,
                        "nombre" varchar(50) NOT NULL,
                        "email" varchar(100) NOT NULL,
                        "asunto" varchar(100) NOT NULL,
                        "mensaje" text NOT NULL,
                        "fecha" timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
                        "leido" boolean NOT NULL DEFAULT FALSE
                    );
                """)
            else:
                cursor.execute("""
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
                """)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS notificaciones_reporte (
                        "idNotificacion" INTEGER PRIMARY KEY AUTOINCREMENT,
                        "titulo" varchar(255) NOT NULL,
                        "contenido_html" text NOT NULL,
                        "tipo" varchar(50) NOT NULL DEFAULT 'DASHBOARD',
                        "fechaCreacion" timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
                        "leida" boolean NOT NULL DEFAULT 0
                    );
                """)
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS mensajes_contacto (
                        "idMensaje" INTEGER PRIMARY KEY AUTOINCREMENT,
                        "nombre" varchar(50) NOT NULL,
                        "email" varchar(100) NOT NULL,
                        "asunto" varchar(100) NOT NULL,
                        "mensaje" text NOT NULL,
                        "fecha" timestamp NOT NULL DEFAULT CURRENT_TIMESTAMP,
                        "leido" boolean NOT NULL DEFAULT 0
                    );
                """)

    def drop_notificaciones_tables(apps, schema_editor):
        """Drop notificaciones tables"""
        with schema_editor.connection.cursor() as cursor:
            cursor.execute("DROP TABLE IF EXISTS mensajes_contacto;")
            cursor.execute("DROP TABLE IF EXISTS notificaciones_reporte;")
            cursor.execute("DROP TABLE IF EXISTS notificaciones_problema;")

    operations = [
        migrations.RunPython(create_notificaciones_tables, drop_notificaciones_tables),
    ]
